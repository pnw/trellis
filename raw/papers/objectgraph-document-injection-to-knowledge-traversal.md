---
title: "ObjectGraph: From Document Injection to Knowledge Traversal — A Native File Format for the Agentic Era"
authors: "Mohit Dubey, Open Gigantic"
source: https://arxiv.org/abs/2604.27820
published: "2026-04-30"
venue: "arXiv preprint"
retrieved: 2026-07-04
---

6
2
0
2

r
p
A
0
3

]
I

A
.
s
c
[

1
v
0
2
8
7
2
.
4
0
6
2
:
v
i
X
r
a

ObjectGraph: From Document Injection to Knowledge Traversal
A Native File Format for the Agentic Era

Mohit Dubey

· Open Gigantic

Abstract

Every document format in existence was designed for a human reader moving linearly through text. Autonomous LLM agents do not
read—they retrieve. This fundamental mismatch forces agents to inject entire documents into their context window, wasting tokens on
irrelevant content, compounding state across multi-turn loops, and broadcasting information indiscriminately across agent roles. We argue
this is not a prompt engineering problem, not a retrieval problem, and not a compression problem: it is a format problem.
We introduce OBJECTGRAPH (.og), a file format that reconceives the document as a typed, directed knowledge graph to be traversed
rather than a string to be injected. OBJECTGRAPH is a strict superset of Markdown—every .md file is a valid .og file—requires no
infrastructure beyond a two-primitive query protocol, and is readable by both humans and agents without tooling.
We formalize the Document Consumption Problem, characterise six structural properties no existing format satisfies simultaneously, and
prove OBJECTGRAPH satisfies all six. We further introduce the Progressive Disclosure Model, the Role-Scoped Access Protocol, and
Executable Assertion Nodes as native format primitives. Empirical evaluation across five document classes and eight agent task types
demonstrates up to 95.3% token reduction with no statistically significant degradation in task accuracy (p > 0.05). Transpiler fidelity
reaches 98.7% content preservation on a held-out document benchmark.

1 Introduction

The past three years have witnessed the rapid deployment of au-
tonomous LLM agents across domains ranging from software
engineering to scientific discovery. These agents—whether or-
chestrating multi-step workflows, maintaining persistent knowl-
edge bases, or coordinating with specialised sub-agents—share
a common dependency: they consume documents. Skill files
describe capabilities. Runbooks encode operational procedures.
Execution plans coordinate multi-agent pipelines. Configu-
ration files constrain behaviour. In nearly every case, these
documents are written in Markdown.

Markdown was designed in 2004 by Gruber [Gruber, 2004]
for human authors producing web content. Its design assump-
tions are deeply human-centric: content is read linearly, from
top to bottom; the reader holds the full document in working
memory; relevance is determined by eye rather than by query.
None of these assumptions hold for LLM agents.

The Core Mismatch. When an agent is invoked with a task—
“deploy the application to staging”—its runtime reads the rele-
vant skill file in its entirety and injects the full content into the
context window. For a typical 600-line deployment runbook,
this costs approximately 1,800 tokens. The content relevant to
the specific task—perhaps 80 tokens—represents a 4.4% util-
isation rate. The remaining 1,720 tokens (95.6%) are wasted
on irrelevant sections, background explanations, and content
scoped to other roles or scenarios.

This waste is not merely expensive; it is structurally harmful.
As agents operate in multi-turn loops—searching, reading, ex-
ecuting, verifying, and searching again—each document read
is appended to the conversation history. Because LLM APIs
are stateless, this history is re-transmitted in full on every sub-
sequent call. A five-turn loop involving three document reads
can compound the original 1,800 tokens into 15,000+, making
the multi-turn overhead exceed the document cost by an order

of magnitude. We formalise this as the Context Compounding
Problem in Section 2.

Prior Approaches and Their Limits. Existing work addresses
adjacent aspects of this problem but not the format itself. Con-
text compression systems [Xiao et al., 2026, Gao et al., 2026]
reduce token counts by removing content, but preserve the in-
jection model and do not eliminate multi-turn compounding.
Retrieval-Augmented Generation (RAG) [Lewis et al., 2020]
retrieves passages from external corpora but requires vector
database infrastructure and cannot encode typed relationships,
executable logic, or access control. Semantic file systems [Mei
et al., 2024] provide LLM-aware file management but require
persistent services. Token-efficient serialisation formats such
as TOON [Schopplich, 2025] reduce structured data payloads
but are not document formats—they encode records, not knowl-
edge.

This Paper. We identify that the problem is not in how
agents process documents but in how documents are struc-
tured. We propose OBJECTGRAPH (.og), a format that treats
the document as a typed knowledge graph whose nodes are
semantic units of information and whose edges are typed
dependency relationships. Agents interact with .og files
through a two-primitive query protocol—search_index
and resolve_context—that retrieves only the nodes rel-
evant to the current task, automatically traversing declared
dependencies, and filtering content by agent role.

Contributions. This paper makes the following contributions:

• A formal model of the Document Consumption Problem and
the six structural properties a format must satisfy to solve it
(Section 2).

• The OBJECTGRAPH format specification: a complete,
human-readable, infrastructure-free document format satisfy-
ing all six properties (Section 4).

1

 
 
 
 
 
 
• The LLM-Native Query Protocol: a two-primitive interface
enabling agents to traverse .og files without loading them
into context (Section 5).

This grows super-linearly in both T and n. A five-turn loop
reading a 1,800-token document once can cost ≈9,000 tokens
in transmission overhead alone.

• A hybrid transpiler converting arbitrary Markdown to .og

with provable content fidelity (Section 6).

• An empirical evaluation across 5 document classes and 8
task types demonstrating 60–95% token reduction without
accuracy loss (Section 8).

F3: Role Blindness.
In multi-agent systems, orchestrator
agents, worker agents, and read-only monitoring agents require
different views of the same document. No existing format
supports role-conditional content serving at the format level;
all consumers receive identical content.

2 The Document Consumption Problem

2.1 Formal Model

Let D be a document of n tokens, partitioned into k semantic
sections D = {s1, s2, . . . , sk} where |si| denotes the token
count of section i and (cid:80)k
i=1 |si| = n. An agent task τ is
associated with a relevance set R(τ ) ⊆ {1, . . . , k} such that
|R(τ )| ≪ k in general.

Definition 1 (Full-Read Assumption). A document format F
satisfies the Full-Read Assumption if the minimum cost of
retrieving any content from a document formatted as F is Ω(n),
i.e. proportional to the total document size regardless of |R(τ )|.

Proposition 1. Markdown, plain text, JSON, YAML, and HTML
all satisfy the Full-Read Assumption.

This follows from the absence of a query-addressable index
in these formats. Without an index, an agent cannot determine
which sections are relevant without reading all of them.

2.2 Three Failure Modes

F1: Token Inflation. The per-query token cost under the Full-
Read Assumption is Cread(τ ) = n regardless of |R(τ )|. Define
the Utilisation Rate as:

U(τ ) =

(cid:80)

i∈R(τ ) |si|
n

(1)

Our empirical analysis of 1,247 real-world agent task execu-
tions across five document classes finds ¯U = 0.063, meaning
agents use on average only 6.3% of injected content. The
remaining 93.7% constitutes pure waste.

F2: Context Compounding. In multi-turn agentic loops, LLM
APIs are stateless: the full conversation history must be re-
transmitted on every call. Let ht denote the history token count
at turn t.
If an agent executes m document reads across a
workflow, the total token cost is:

Ctotal =

T
(cid:88)

t=1

ht =



h0 +



cj



(cid:88)

j≤t

T
(cid:88)

t=1

(2)

where cj is the cost of operation j and h0 is the initial context.
For m document reads, each costing n tokens, in a T -turn
workflow:

Ccompound = T · h0 + m · n · (T − tread + 1)

(3)

2.3 Six Required Properties

We derive six necessary properties from the three failure modes:

Definition 2: Required Properties for Agent-Native Docs

P1 Query-Addressable Index: O(1) mapping from semantic

query to relevant section identifiers.

P2 Layered Compression: Multiple fidelity levels (summary, full,

code) natively encoded per section.

P3 Typed Dependency Graph: Explicit, machine-traversable

relationships between sections.

P4 Role-Scoped Access Control: Content filtered by consumer

role at format level, without external middleware.

P5 Executable Assertions: Validation conditions, retry logic, and

escalation paths encoded in the document.

P6 Human Readability: Directly authored and read by humans

without compilation or tooling.

Table 1 positions OBJECTGRAPH against prior formats

across these six properties.

Table 1: Property satisfaction matrix across formats. ✓ = full,
◦ = partial, × = absent.

Format

P1 P2 P3 P4 P5 P6

Markdown
JSON / YAML
TOON
llms.txt
GraphRAG
LSFS
SkillReducer

×
×
×
×

×
◦
×
×

×
×
×
×
×
×
◦
×
✓ × ✓ ×
✓ ×
×
◦
◦
×

◦
×

× ✓
◦
×
◦
×
× ✓
×
×
×
×
× ✓

OBJECTGRAPH ✓ ✓ ✓ ✓ ✓ ✓

3 Related Work

Context Compression. A substantial body of work addresses
token reduction through content removal. Xiao et al. [2026]
remove useless, redundant, and expired information from agent
trajectories, achieving 39.9–59.7% input token reduction on
coding agents. Gao et al. [2026] report 48% description com-
pression and 39% body compression through progressive dis-
closure in skill bodies. Huang et al. [2025] achieve 22.7%
reduction through autonomous compression during execution.
Critically, these approaches compress content within the injec-

2

tion model; they do not eliminate full-reads or context com-
pounding, because the document format remains unchanged.

Structured Knowledge for Agents. Shi et al. [2025] evalu-
ate schema representation formats (YAML, Markdown, JSON,
TOON) for file-native agentic systems. Their evaluation covers
SQL generation accuracy, finding that no single format domi-
nates across model tiers. TOON [Schopplich, 2025] achieves
25–46% token reduction over JSON for structured data pay-
loads, but explicitly targets record serialisation rather than
document representation and provides no graph traversal, de-
pendency resolution, or human authoring model.

Graph-Based Knowledge. Edge et al. [2024] construct entity
graphs from document corpora for global search; their approach
requires vector databases and offline indexing pipelines, mak-
ing it unsuitable as a general-purpose document format. Shi
et al. [2026] build knowledge graphs from code repositories
using tree-sitter, achieving structural retrieval advantages but
restricted to code corpora. FatCat [2025] propose a document-
driven multi-agent system using Markdown as a “high-SNR
semantic file system”, noting that Markdown’s alignment with
LLM pretraining priors reduces attention dilution—a key moti-
vation for our Markdown superset design.

File-Native Agent Context. The industry has converged
on file-based context patterns: CLAUDE.md, AGENTS.md,
CURSOR.rules, and llms.txt [llms.txt, 2024]. These are
statically read, entirely injected, and provide no query inter-
face. They represent the state of practice that OBJECTGRAPH
directly supersedes.

Skill Representation.
Jiang et al. [2026] introduce the
Scheduling-Structural-Logical (SSL) representation for agent
skills, drawing on classical knowledge representation theory.
Their work addresses the internal structure of skills but does not
address the file format through which skills are stored, retrieved,
or consumed at runtime. OBJECTGRAPH is complementary:
SSL-structured skills can be stored as .og nodes.

4 The ObjectGraph Format

4.1 Core Abstraction

OBJECTGRAPH models a document as a directed, typed graph
G = (V, E, λ, ρ) where:
• V is a set of nodes, each representing a self-contained seman-

tic unit of knowledge.

• E ⊆ V × V is the edge set of typed dependencies.

• λ : E → L is an edge labelling function over a typed label

set L (e.g., :requires, :precedes).

4.2 File-Level Structure

Every .og file begins with three mandatory blocks read during
the index pass.

Listing 1: File-level manifest of an .og document.

1 ::meta
2

Python Deployment Runbook

title:
version: 2.3.0
updated: 2025-04
domain:
scope:
checksum: sha256:a3f9c2...

deployment|python|devops
all

node-types: [concept,step,warning,

12

13

14

edge-types:

example,assertion,meta]
[requires,precedes,

see-also,supersedes]

scope-levels:[all,orchestrator,worker]

7
8 ::end
9
10 ::schema
11

15
16 ::end
17
18 ::index
19

# id
install

3

4

5

6

20

21

22

23

24

25

26

|type |scope
|step |all

|conf|keywords
|0.99|install,pip,venv,

setup

configure

|step |all

|0.97|config,env,

variables

deploy-prod

|step |all

|0.95|deploy,prod,

release

api-keys
key
troubleshoot
post-install

assert
__changelog

updates

|step |orchestrator|0.99|vault,secret,api,

|step |all
|assert|all

|0.90|error,debug,fail
|1.00|verify,check,

|meta |all

|1.00|changes,diff,

27 ::end

The ::index block is the critical innovation. At approxi-
mately 30 tokens for a typical skill file, it provides a complete
routing table that an agent can read to determine task relevance
without loading any content nodes.

4.3 The Node: Atomic Knowledge Unit

Every semantic unit in an .og file is a node—a typed container
with a stable identifier, scope annotation, confidence score, and
versioning metadata:

n = ⟨id, type, conf, scope, updated, content_blocks, edges⟩

(4)
The node identifier is immutable across versions, enabling
cross-document edge references and diff-based delta loading
(Section 4.9).

4.4 Content-Type Tags: Richer than Markdown

• ρ : V → S is a scope function mapping nodes to access roles

S (e.g., all, orchestrator, worker).
The file-level structure serves as the graph’s manifest: a
lightweight, always-read header that enables O(1) node discov-
ery before any content is loaded.

A fundamental limitation of Markdown is that content type is
encoded only visually—a code fence, a blockquote, and a bullet
list look different to a human but are semantically indistinguish-
able to an agent. OBJECTGRAPH introduces explicit semantic
type annotations for every content block.

Table 2 provides the complete taxonomy.

3

Listing 2: A complete node demonstrating all content layers.

Table 2: ObjectGraph content-type tags and their semantic
contracts.

1 ::node[id=install type=step
2

confidence=0.99 scope=all
updated=2025-04 entry=true]

3

4
5 ::dense
6 python3.11+|pip|venv|requirements.txt|
7 activate|--break-system-packages
8 ::end
9
10 ::full
11 Ensure Python 3.11+ is installed.
12 Create and activate a virtual environment
13 before installing project dependencies.
14 ::end
15
16 ::steps
17 1. python -m venv .venv
18 2. source .venv/bin/activate # Linux/Mac
19 3. .venv\Scripts\activate
20 4. pip install -r requirements.txt
21 ::end
22
23 ::code[lang=bash]
24 python -m venv .venv
25 source .venv/bin/activate
26 pip install -r requirements.txt
27 ::end
28
29 ::warning
30 Never install packages globally.
31 Virtual environment isolation prevents
32 dependency conflicts across projects.
33 ::end
34
35 ::edges
36

# Windows

->[:precedes] configure
->[:precedes] post-install
->[:requires] concept-virtualenv

37

38
39 ::end
40
41 ::end # install

Tag

Semantic Meaning

Behaviour

::dense
Compressed keyword summary Always; Pass 2
::full
Complete prose explanation
::code[lang] Executable/technical content
::steps
::list
::table
::warning
::note
::example
::reference
::assertion
::summary

Ordered sequential actions
Unordered enumeration
Structured relational data
Critical safety information
Informational aside
Concrete illustration
External citation or URL
Executable validation logic
Human-authored précis

Pass 3
Verbatim
Order kept
Any order
Verbatim
Never skip
Optional
Skippable
On demand
Post-exec
Alt. dense

For typical values (n = 1,800, |M (τ )| = 2, |F (τ )| = 1):
Cog = 30 + 2·12 + 1·180 = 234, yielding Savings = 87.0%.

4.6 Typed Edge Declarations
Edges are declared within each node’s ::edges block using
a concise directed-graph syntax:

Listing 3: Edge syntax with conditional edges.

1 ::edges
2

->[:precedes]
configure
->[:requires]
concept-virtualenv
deploy-prod
<-[:used-in]
<>[:related]
troubleshoot
->[:see-also condition=’query contains k8s’]

3

4

5

6

4.5 The Progressive Disclosure Model

The Progressive Disclosure Model (PDM) is the central mech-
anism by which OBJECTGRAPH eliminates token inflation.
Every node exposes three reading depths:

Pass 1 — Index Pass (∼30 tokens, fixed)
Read ::meta + ::index. Determine which nodes are relevant.

Pass 2 — Dense Pass (∼10–15 tokens/node)
Read ::dense blocks of matched nodes. Sufficient for routing
and planning decisions.

Pass 3 — Full Pass (∼100–300 tokens/node)
Read ::full, ::code, ::steps, etc. Required only for task
execution.

The cost model for a single query τ is:

Cog(τ ) = Cindex + |M (τ )| · ¯cd + |F (τ )| · ¯cf

(5)

where M (τ ) is the set of matched nodes read at dense level,
F (τ ) ⊆ M (τ ) is the subset requiring full-pass reading, ¯cd ≈
12 tokens, and ¯cf ≈ 180 tokens. Comparing to the baseline
Cmd(τ ) = n:

7
8 ::end

kubernetes-deploy

:contradicts,

The label set L includes: :requires, :precedes,
:elaborates,

:contains,
:see-also, :supersedes, :used-in.
Automatic Dependency Traversal. When the query proto-
col resolves a node, it automatically follows all :requires
edges and fetches prerequisite nodes. This means an agent
querying “deploy to production” receives not only the deploy
node but also its declared dependencies (e.g., configure, api-
keys), without issuing additional queries.

4.7 Role-Based Access Control
The scope attribute on both index entries and nodes imple-
ments a first-class role-based access control layer at the format
level. The ::index exposes scope information in Pass 1, so
an agent with role r never even learns of the existence of nodes
with ρ(n) /∈ {r, all}.

This eliminates the need for external access control middle-
ware in document-serving pipelines—a significant reduction in
system complexity for multi-agent deployments.

4.8 Executable Assertion Nodes

Savings(τ ) = 1 −

Cog(τ )
n

Assertion nodes encode validation logic, retry routing, and
escalation paths directly in the document. They are triggered

(6)

4

Listing 4: Role-scoped nodes serving different consumers from
the same file.

type=step confidence=1.0]

1 # Orchestrator agent sees real credentials
2 ::node[id=api-keys scope=orchestrator
3
4 ::full
5 Retrieve production API key from Vault:
6 vault kv get secret/prod/api-key
7 ::end
8 ::end
9
10 # Worker agent receives a safe abstraction
11 ::node[id=api-keys scope=worker
12
13 ::full
14 API keys are managed by the orchestrator.
15 Request credentials via:
16
17 ::end
18 ::end

get_secret(’prod/api-key’)

type=step confidence=1.0]

by the query protocol after the designated predecessor node
completes:

Listing 5: An assertion node encoding post-installation verifi-
cation.

1 ::node[id=post-install type=assertion]
2 ::assertion
3

trigger:
check:

after[install]
command(’python --version’)
matches ’Python 3\.1[0-9]’
file_exists(’.venv/bin/activate’)
->[:proceed] configure
->[:retry limit=2] install

check:
on-pass:
on-fail:
on-fail-after-retries:

4

5

6

7

8

9

10

->[:escalate] troubleshoot
30s

timeout:

11
12 ::end
13 ::end

Assertion nodes eliminate the need to encode validation logic
in agent prompts, reducing prompt length and separating what
to do (in nodes) from whether it succeeded (in assertions).

4.9 Delta Loading via Changelog
The ::changelog meta-node enables incremental document
consumption. An agent that has previously read a document
at version v can determine all changes since v by reading only
the changelog node (∼30 tokens), then fetching only the delta
nodes:

Listing 6: Changelog node enabling delta-based document
updates.

1 ::node[id=__changelog type=meta]
2 ::changelog
3

2025-04-15|added
2025-04-10|updated|node[install]
2025-03-01|deprecated|node[heroku-deploy]

|node[kubernetes-deploy]

4

5
6 ::end
7 ::end

Proposition 2. For a document updated at rate µ (nodes/-
month) and consumed q times between updates, delta loading
reduces update-check cost from O(n) to O(µ · ¯cf ).

4.10 Backward Compatibility

OBJECTGRAPH is a strict superset of Markdown:

5

Theorem 1 (Backward Compatibility). Every valid Markdown
document is a valid .og document. Specifically, a Markdown
document D parsed as .og is equivalent to a single-node
.og document with D’s content in a ::full block, with no
::index, ::dense, or ::edges blocks. Agents fall back
to full-read behaviour with zero errors.

This means adoption requires no migration of existing
documents—they gain .og capabilities incrementally as au-
thors add structured blocks.

5 The LLM-Native Query Protocol

5.1 Design Rationale

The query protocol is deliberately minimal: two primitives,
exposed as MCP tools [Anthropic, 2024] or function-calling
schemas. More primitives would reintroduce the complexity
they are meant to eliminate; fewer would sacrifice either the
index-first routing or automatic dependency resolution.

Definition 3: The Two-Primitive Query Protocol

Primitive 1: search_index(f , q, r)
Given file path f , natural language query q, and agent role r,
returns a formatted index string listing all node IDs whose key-
words overlap with q and whose scope includes r. Token cost:
O(Cindex).

Primitive 2: resolve_context(f , N )
Given file path f and a set of node IDs N , returns the full content
of all nodes in N plus all nodes reachable via :requires edges
within a declared depth limit. Token cost: O(|N | · ¯cf + |Er| · ¯cf )
where Er is the set of required dependency nodes.

5.2 LLM as Router
A critical insight is that the index search is performed by the
LLM, not by a keyword-matching algorithm. The agent reads
the index string and uses its full semantic understanding to
decide which nodes are relevant—far superior to BM25 or em-
bedding similarity for the structured, domain-specific content
of agent files. This pattern, which we term LLM-as-Router,
requires no fine-tuning: any instruction-following model can
perform it from a one-paragraph system prompt addition.

Algorithm 1 provides the full query workflow.

5.3 Architectural Instantiations

OBJECTGRAPH supports two architectures depending on docu-
ment scale:

Architecture A: One-Shot Injection (small files, n < 10k
tokens). The ::index block (∼150 tokens) is injected
into the system prompt at session start. The agent calls
resolve_context exactly once per task. No search tool
call, no multi-turn compounding. Total protocol overhead:
zero.

Architecture B: Router/Executor Delegation (large files,
n ≥ 10k tokens). A lightweight Router agent (e.g., Claude
Haiku) receives search_index and outputs a JSON array of
node IDs. The orchestration layer calls resolve_context
locally. An Executor agent (e.g., Claude Sonnet) receives only

Algorithm 1: ObjectGraph Query Protocol

Input: File f , task description τ , agent role r, session S
Output: Context payload P

1 index ← parse_index(f , role=r);
2 candidates ← filter_by_confidence(index,

θ = 0.80);

3 N ← LLMROUTER(candidates, τ );

selects node IDs */

/* LLM

4 N ← N \ S.visited; /* skip-if-known filter

*/

5 deps ← resolve_edges(f , N , :requires);
6 Nfull ← N ∪ deps;
7 for ni ∈ Nfull do
8

if has_warning(ni) then

9

10

11

12

13

14

15

16

P ← P ∪ fetch_full(f , ni);

end
else if τ requires execution then

P ← P ∪ fetch_full(f , ni);

end
else

P ← P ∪ fetch_dense(f , ni);

end
S.visited ← S.visited ∪ {ni};

17
18 end
19 return P ;

Architecture A (small files)
1 call

Agent

reads once

Index
(system
prompt)

resolve_
context

Architecture B (large files)

Router
Agent

query

search_
index

node IDs

resolve_
context

nosharedhistory

payload only

Executor
Agent

Figure 1: Two architectural instantiations of the ObjectGraph
query protocol. Architecture B eliminates context compound-
ing by design: the Executor agent receives zero tool-call history.

6.2 Stage 1: Deterministic Structural Extraction

Algorithm 2 describes the rule-based parser. It operates as a
single-pass state machine with O(n) complexity.

Table 3 summarises the Markdown-to-OBJECTGRAPH map-

ping rules.

the resolved context payload—zero tool-call history, zero com-
pounding. Figure 1 illustrates both architectures.

5.4 Session Memory and Skip-If-Known
The session object S maintains a visited-node set across turns.
Nodes annotated with skip-if-known=true (typically
concept nodes explaining foundational background) are
fetched at most once per session, regardless of how many times
they appear in subsequent dependency traversals.

6.3 Stage 2: Bounded LLM Metadata Synthesis
For each node ni, a single LLM call generates the ::dense
block (8–12 pipe-separated keywords) and ::index query
terms. The prompt is deliberately constrained: the LLM re-
ceives only the ::full prose blocks (never code or table
content) and is instructed to produce keywords rather than para-
phrase. This bounds hallucination exposure to navigational
metadata.

Proposition 3 (Session Savings). In a workflow visiting k
distinct nodes across T turns, with a fraction α of nodes
marked skip-if-known, the session savings relative to
turn-independent reading is:

Stage 2 LLM Prompt Template

You are generating search index keywords.
Node:
Prose content:

{node_id} | Type: {node_type}
{full_content[:500]}

∆session = α · k · (T − 1) · ¯cf

(7)

DENSE (max 15 tokens, pipe-separated
technical

For α = 0.3, k = 10, T = 5, ¯cf = 180: ∆session = 2,160
tokens saved in addition to per-query savings.

6 The Transpiler: Markdown to ObjectGraph

6.1 Design Principles
The transpiler converts arbitrary Markdown documents to .og
through a three-stage hybrid pipeline grounded in one invari-
ant: LLMs never touch actual content. LLMs generate only
navigational metadata (::dense blocks and ::index key-
words). All content is copied verbatim by deterministic parsers,
bounding hallucination risk to routing pointers rather than in-
formation.

keywords, no verbs, no articles):

INDEX (5-8 comma-separated query terms,

include synonyms):

Respond with exactly two lines.
No explanation.

No markdown formatting.

6.4 Stage 3: Fidelity Verification

The verification pass is deterministic and non-negotiable. It
produces a fidelity score ϕ ∈ [0, 1] and blocks deployment if
ϕ < 0.95.

ϕ =

cp
ct

− α · |A|

(8)

6

Algorithm 2: Stage 1: Rule-Based Structural Extrac-
tion
Input: Markdown document D
Output: Node list N

1 N ← []; ncur ← ∅;
2 foreach line ℓ in D do
3

if ℓ matches /## .+/ then

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

close(ncur); append to N ;
ncur ← NEWNODE(slugify(ℓ));

else if ℓ matches /“‘[\w]*/ then
b ← READVERBATIMBLOCK();
ncur.ADDBLOCK(code, b);
else if ℓ matches /\|.+\|/ then
b ← READTABLEBLOCK();
ncur.ADDBLOCK(table, b);
else if ℓ matches /^\d+\./ then
b ← READSTEPBLOCK();
ncur.ADDBLOCK(steps, b);

else if ℓ starts with > [!WARNING] then

b ← READWARNINGBLOCK();
ncur.ADDBLOCK(warning, b);

else

ncur.APPENDFULL(ℓ);

end

20
21 end
22 return N ;

where cp is the number of checks passed, ct is the total
number of checks, A is the set of content elements found in
.og but not in the source Markdown (hallucinated additions),
and α = 0.02 is the per-addition penalty.

Checks include: (i) every code block present verbatim, (ii) ev-
ery table row preserved, (iii) every heading mapped to a node
ID, (iv) no content in ::full blocks absent from the source.

7 Use Cases

OBJECTGRAPH is a general-purpose document format appli-
cable wherever Markdown is used today. We describe six
primary use cases, each unlocking capabilities impossible with
flat Markdown.

UC1: Agent Skill Files. The motivating use case. Skills
written as .og nodes allow multi-agent frameworks to route
tasks to the relevant procedure without injecting the entire skill
library. A skill library of 50 files (∼90,000 tokens total) is
navigable via a combined index of ∼1,500 tokens.

UC2: Operational Runbooks. Enterprise runbooks frequently
exceed 100,000 tokens. Under the full-read model, reading
a runbook to answer “how do I roll back a failed Kubernetes
deployment?” costs 100k tokens. Under OBJECTGRAPH, the
index pass costs ∼200 tokens; context resolution costs ∼600
tokens. Reduction: 99.2%.

UC3: Agent Execution Plans. Multi-step agent plans ex-

7

Table 3: Markdown to ObjectGraph structural mapping rules.

Markdown Element

OBJECTGRAPH Tag Treatment

::node[id=slug] Node boundary
::code[lang=X]
::table
3. ordered ::steps

Verbatim
Verbatim
Order kept
Verbatim
Verbatim
Verbatim
If standalone
Verbatim
No extraction

::list
::warning
::note
::reference
::full
In ::full

## heading
“‘lang...“‘
| table |
1.
2.
- bullet
> [!WARNING]
> [!NOTE]
[text](url)
Paragraph prose
**bold**

pressed in .og encode not just steps (::steps) but depen-
dencies (::edges), success criteria (::assertion), and
role assignments (scope). Plans become self-verifying: each
step asserts its own completion before the next is resolved.

UC4: Technical Documentation. API documentation, archi-
tecture guides, and onboarding manuals stored as .og allow
both human authors (who see normal Markdown rendering)
and agent consumers (who use the query protocol) to interact
with the same source file. No dual-maintenance of human and
machine versions.

UC5: Multi-Agent Communication Substrates. In multi-
agent pipelines, .og files serve as the shared knowledge
medium. Role-scoped nodes ensure that orchestrator agents,
worker agents, and monitoring agents each receive precisely
the information relevant to their function, from a single source
of truth.

UC6: Knowledge Base Maintenance. The ::changelog
and confidence attributes enable knowledge bases to sig-
nal their own freshness. Automated staleness detection
(updated > k months ago) triggers human review workflows
without requiring external metadata tracking.

8 Evaluation

8.1 Experimental Setup

Document Corpus. We constructed a benchmark of 240 doc-
uments across five classes: Skill Files (48), Operational Run-
books (52), Execution Plans (44), Technical Documentation
(56), and Knowledge Bases (40). Documents ranged from 200
to 15,000 tokens (mean 2,340; median 1,680).
Task Suite. We defined 8 task types: information lookup, pro-
cedure execution, multi-step planning, role-conditional access,
cross-node reasoning, update detection, assertion verification,
and multi-agent handoff. Each document-task pair was exe-
cuted 5 times; we report means and 95% CI.
Models. We evaluate with Claude Sonnet 4.5 (primary), Claude
Haiku 4.5 (Router in Architecture B), and GPT-4o (cross-model
validation).
Baselines. (B1) Full Markdown injection; (B2) RAG with text-

embedding-3-large; (B3) SkillReducer-optimised Markdown.

8.2 RQ1: Token Consumption

mitigated by the automatic dependency traversal mechanism
(reducing the gap from 4.2% to 1.8% with edge declarations).

Figure 2 reports token consumption across document classes
and task types. OBJECTGRAPH reduces mean token consump-
tion from 2,340 to 187 tokens (92.0% reduction; p < 0.001).

Table 4: Task accuracy (%) across methods. OBJECTGRAPH(E)
denotes OBJECTGRAPH with explicit edge declarations. † p <
0.05 vs. Markdown baseline.

y
r
e
u
q

r
e
p

s
n
e
k
o
t

.

g
v
A

6,000

5,000

4,000

3,000

2,000

1,000

0

Markdown (B1)

RAG (B2)

OBJECTGRAPH Arch.A

OBJECTGRAPH Arch.B

Skills

Runbooks

ExecPlans

TechDocs

KB

Figure 2: Mean token consumption per query across docu-
ment classes and approaches. OBJECTGRAPH Architecture B
achieves the greatest reduction on large runbooks.

8.3 RQ2: Context Compounding Reduction

We measured total tokens transmitted across a 5-turn agentic
workflow, each turn involving one document interaction. Fig-
ure 3 shows cumulative token cost as a function of turn number.

)
3
0
1
×

(

s
n
e
k
o
t

e
v
i
t
a
l
u
m
u
C

50

40

30

20

10

0

1

Markdown (B1)
RAG (B2)
OBJECTGRAPH Arch.A
OBJECTGRAPH Arch.B

2

3

4

5

Turn number

Figure 3: Cumulative token cost in a 5-turn agentic work-
flow. Markdown exhibits super-linear compounding. OBJECT-
GRAPH Architecture B maintains near-linear growth through
context isolation.

At turn 5, Markdown has accumulated 46,000 tokens ver-
sus OBJECTGRAPH Architecture B’s 1,260 tokens—a 36.5×
reduction. The super-linear growth of Markdown is clearly
visible; OBJECTGRAPH Arch. B is near-linear due to context
isolation.

8.4 RQ3: Task Accuracy

Table 4 reports task accuracy across methods and task types.
OBJECTGRAPH matches or exceeds Markdown accuracy on 7
of 8 task types. The single exception—Cross-node reasoning,
where Markdown’s full injection provides implicit context—is

8

Task Type MD RAG OBJECTGRAPH OBJECTGRAPH(E)

Information
lookup
Procedure
execution
Multi-step
planning
Role-
conditional
Cross-node
reasoning
Update de-
tection
Assertion
verify
Multi-agent
handoff

91.2

87.4

88.6

83.1

84.3

79.8

76.4

71.2

82.1

74.6

61.3

54.7

52.8

48.1

71.4

69.3

92.1†

89.4†

85.7†

94.8†

77.9

91.4†

96.3†

93.2†

Mean

76.0

71.0

90.1

92.3†

90.1†

86.2†

95.1†

80.3

91.6†

96.5†

94.1†

90.8

The dramatic improvement on Role-conditional access
(+18.4%), Update detection (+30.1%), and Assertion verifi-
cation (+43.5%) reflects capabilities absent in Markdown that
OBJECTGRAPH encodes natively.

8.5 RQ4: Transpiler Fidelity

The transpiler was evaluated on 180 held-out documents not
in the task benchmark. Mean fidelity ¯ϕ = 0.987 (SD = 0.018).
Failures concentrated in two cases: deeply nested blockquotes
(which Stage 1 flattens) and multi-paragraph code comments
(misclassified as prose). Both are addressed in post-processing.
No document fell below the ϕ = 0.95 deployment threshold
after human review.

8.6 RQ5: Human Authoring Burden

We conducted a user study with 18 participants (12 software
engineers, 6 technical writers) who authored .og files from
scratch using only the specification and a one-page cheat sheet.
Participants rated authoring burden on a 7-point Likert scale.
Mean burden: 2.8/7 (SD=1.1). Qualitatively, participants noted
that the explicit content-type tags (::warning, ::steps,
::code) felt “more descriptive than Markdown” and that the
::dense constraint “forced better documentation discipline.”

8.7 Ablation Study

Figure 4 shows the contribution of individual OBJECTGRAPH
features to token reduction, isolating the effect of each compo-
nent.

Full OBJECTGRAPH

92

Index routing

28

Delta loading

14

Role scoping

8

Skip-if-known

12

Dense layer

18

0

20

40

60

80

100

Token reduction (%)

Figure 4: Ablation: token reduction contribution of individual
OBJECTGRAPH features. Index routing and the dense layer
account for 82% of total savings.

9 Discussion

9.1 The Less-Is-More Effect

A counterintuitive finding is that OBJECTGRAPH not only re-
duces token cost but improves accuracy on most task types.
We attribute this to two mechanisms. First, the elimination of
irrelevant content reduces attention dilution—a phenomenon
documented by Gao et al. [2026], who found that removing
non-essential content improves task performance by 2.8% even
at equivalent token budgets. Second, the semantic content-type
tags (::warning, ::steps) provide structural signals that
improve the model’s parsing accuracy, an effect consistent with
Shi et al. [2025]’s finding that structured formats improve agent
task performance on file-native systems.

9.2 ObjectGraph as Infrastructure

We note that OBJECTGRAPH’s adoption implications extend be-
yond token savings. Role-scoped nodes eliminate the need for
document access control middleware in multi-agent pipelines.
Executable assertions eliminate the need for separate valida-
tion prompt templates. Delta loading eliminates the need for
document change tracking systems. In each case, functionality
previously requiring external infrastructure is encoded in the
document format itself, reducing system complexity and the
surface area for failure.

9.3 Limitations

Evaluation Scale. Our benchmark of 240 documents, while
carefully curated, does not cover the full diversity of real-world
document types. Evaluation on enterprise-scale corpora re-
mains future work.
Multi-file Federation. The current specification does not sup-
port cross-file edge resolution—edges referencing nodes in
other .og files. This limits OBJECTGRAPH’s applicability to
mono-repo or single-domain knowledge bases.
Standardisation. Without a standards body or broad commu-
nity adoption, the format risks fragmentation into incompatible
dialects. We recommend an RFC-style governance process as a
near-term priority.

9

Adversarial Inputs. We have not evaluated OBJECTGRAPH
against adversarial document authors who might craft mislead-
ing ::dense blocks or ::index entries to manipulate agent
routing.

10 Conclusion

We introduced OBJECTGRAPH, a document format that recon-
ceives the Markdown document as a typed knowledge graph
traversable by LLM agents. By formalising the Document
Consumption Problem and deriving six structural properties
necessary for its solution, we demonstrated that no existing
format satisfies all six simultaneously, and that OBJECTGRAPH
does. Through the Progressive Disclosure Model, the two-
primitive LLM-Native Query Protocol, role-scoped access con-
trol, and executable assertion nodes, OBJECTGRAPH reduces
agent token consumption by 60–95% with no accuracy penalty,
while remaining directly authored and read by humans without
tooling.

The open problem is federation: a standardised protocol for
cross-file edge resolution that would enable .og documents
to form a distributed knowledge graph spanning repositories,
organisations, and agent ecosystems. This, we believe, is the
natural next step toward a structured, queryable substrate for
the agentic web.

References

Anthropic. Model Context Protocol (MCP): An open standard for
connecting AI assistants to tools and data sources, 2024. https:
//modelcontextprotocol.io.

D. Edge, H. Trinh, N. Cheng, J. Bradley, A. Chao, A. Mody, S. Truitt,
and J. Larson. From local to global: A graph RAG approach to
query-focused summarization. arXiv preprint arXiv:2404.16130,
2024.

Anonymous. Fat-Cat: Document-driven metacognitive multi-agent
system for complex reasoning. arXiv preprint arXiv:2602.02206,
2025.

Y. Gao, Z. Li, Y. Yuan, Z. Ji, P. Ma, and S. Wang. SkillReducer:
Optimizing LLM agent skills for token efficiency. arXiv preprint
arXiv:2603.29919, 2026.

J. Gruber. Markdown, 2004. https://daringfireball.net/

projects/markdown/.

Anonymous. Active context compression: Autonomous memory
management in LLM agents. arXiv preprint arXiv:2601.07190,
2025.

Anonymous. From skill text to skill structure: The Scheduling-
Structural-Logical representation for agent skills. arXiv preprint
arXiv:2604.24026, 2026.

P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,
H. Küttler, M. Lewis, W.-T. Yih, T. Rocktäschel, S. Riedel, and
D. Kiela. Retrieval-augmented generation for knowledge-intensive
NLP tasks. In Advances in Neural Information Processing Systems
(NeurIPS), 2020.

J. Howard. A proposed standard for using Markdown in LLM context,

2024. https://llmstxt.org.

W. Mei, Y. Guo, Y. Wang, Z. Li, and H. Zhao. From commands to
prompts: LLM-based semantic file system for AIOS. arXiv preprint
arXiv:2410.11843, 2024.

J. Schopplich. TOON: Token-Oriented Object Notation, 2025.

https://toonformat.dev.

Anonymous. Structured context engineering for file-native agentic

systems. arXiv preprint arXiv:2602.05447, 2025.

Anonymous. Codebase-Memory: Tree-Sitter-based knowledge
arXiv preprint

graphs for LLM code exploration via MCP.
arXiv:2603.27277, 2026.

Y.-A. Xiao, P. Gao, C. Peng, and Y. Xiong. Reducing cost of
LLM agents with trajectory reduction. Proc. ACM Softw. Eng.,
3(FSE):FSE056, 2026.

10

A Complete ObjectGraph Format Specification

Normative Tag Reference

Tag

Level

Pass

Required

Semantic Contract

::meta
File
::index
File
::schema
File
::node[...]
Container
::dense
Content
::full
Content
::code[lang] Content
::steps
Content
::list
Content
::table
Content
::warning
Content
::note
Content
::example
Content
::reference
Content
::assertion
Behaviour
::edges
Navigation
::traverse
Navigation
::changelog
Meta
::end
Structural

1
Yes
1
Yes
1
No
Any
Yes
2
Yes
3
Yes
3
No
3
No
3
No
3
No
2+
No
3
No
3
No
No
3
Runtime No
No
2
No
1
No
1
Yes
Any

Machine-readable file metadata
Complete node routing table
Type and edge-type declarations
Typed node with attributes
≤15-token keyword compression
Complete verbatim prose
Executable content; never summarised
Ordered sequential actions
Unordered enumeration
Relational data; never paraphrased
Always read; never skipped
Optional informational aside
Skippable concrete illustration
External citation with URL
Post-execution validation logic
Typed outbound/inbound edges
Traversal hint metadata
Structured delta-loading log
Block terminator (universal)

B Token Cost Model Derivation
Let D be an .og document with k nodes indexed in ::index. Define:

Cindex = cmeta + k · centry ≈ 30 + 6k tokens

Cdense(ni) ≈ 15 tokens (worst case)
| + |nsteps
Cfull(ni) = |nfull

| + |ncode

|

i

i

i

For a query matching m nodes at dense level and p ≤ m at full level:

Cog = Cindex + m · Cdense + p · E[Cfull]

The savings ratio over full Markdown injection:

Σ = 1 −

Cog
n

= 1 −

30 + 6k + 15m + 180p
n

Assuming k = 10, m = 2, p = 1, n = 1800: Σ = 1 − (30 + 60 + 30 + 180)/1800 = 1 − 300/1800 = 83.3%.

C Complete Deployment Runbook Example

Listing 7: Production-ready .og deployment runbook demonstrating all format features.

(9)

(10)

(11)

(12)

(13)

Python Application Deployment Runbook

title:
version: 2.3.0 author: devops-team
updated: 2025-04
scope:

all checksum: sha256:a3f9c2b1d8...

domain: deployment|python|devops

node-types:
edge-types: [precedes,requires,see-also,supersedes]
scope-levels:[all,orchestrator,worker,readonly]

[concept,step,warning,example,assertion,meta]

1 ::meta
2

3

4

10

5
6 ::end
7
8 ::schema
9

11
12 ::end
13
14 ::index

11

15

16

17

18

19

20

21

22

23

24

|conf|keywords

|type |scope
# id
|step |all
install
|step |all
configure
|step |all
deploy-prod
|step |all
deploy-staging
|step |all
rollback
|step |orchestrator |0.99|vault,secret,api,key,credentials
api-keys
|step |worker
api-keys-worker
|step |all
troubleshoot
post-install-check|assert|all
|meta |all
__changelog

|0.99|install,pip,venv,setup,python
|0.97|config,env,variables,settings
|0.95|deploy,production,release,ship
|0.95|staging,test,preview,sandbox
|0.93|rollback,revert,undo,restore

|0.99|api,key,credentials,access
|0.90|error,debug,fail,broken,crash
|1.00|verify,check,assert,validate
|1.00|changes,diff,updates,version

25
26 ::end
27
28 ::node[id=install type=step confidence=0.99 scope=all updated=2025-04 entry=true]
29 ::dense
30 python3.11+|pip|venv|requirements.txt|activate|--break-system-packages
31 ::end
32 ::full
33 Ensure Python 3.11 or higher is installed on the target system.
34 Create and activate a virtual environment before installing dependencies.
35 ::end
36 ::steps
37 1. Create environment: python -m venv .venv
38 2. Activate (Linux/Mac): source .venv/bin/activate
39 3. Activate (Windows):
40 4. Install dependencies: pip install -r requirements.txt
41 5. System Python only:
42 ::end
43 ::warning
44 Never install packages globally into the system Python. Virtual environment
45 isolation is mandatory for reproducible deployments and prevents dependency conflicts.
46 ::end
47 ::code[lang=bash]
48 python -m venv .venv && source .venv/bin/activate
49 pip install -r requirements.txt
50 python --version && pip list | grep -E "requests|fastapi"
51 ::end
52 ::edges
53

add --break-system-packages flag

.venv\Scripts\activate

54

->[:precedes] configure
->[:precedes] post-install-check
->[:requires] concept-virtualenv

55
56 ::end
57 ::end # install
58
59 ::node[id=post-install-check type=assertion]
60 ::dense
61 verify|python3.11|pip|venv|assert|check
62 ::end
63 ::assertion
64

65

66

67

68

69

70

71

after[install]
command(’python --version’) matches ’Python 3\.1[0-9]’
command(’pip list’) contains ’requests’
file_exists(’.venv/bin/activate’)
->[:proceed] configure
->[:retry limit=2] install

trigger:
check:
check:
check:
on-pass:
on-fail:
on-fail-after-retries: ->[:escalate] troubleshoot
max-retries: 2
timeout:

30s

72
73 ::end
74 ::end # post-install-check
75
76 ::node[id=api-keys type=step confidence=1.0 scope=orchestrator updated=2025-04]
77 ::dense
78 vault|prod-api-key|kv-secret|orchestrator-only
79 ::end
80 ::full
81 Retrieve the production API key from the internal Vault instance.
82 ::end
83 ::code[lang=bash]
84 vault kv get secret/prod/api-key
85 export API_KEY=$(vault kv get -field=value secret/prod/api-key)
86 ::end
87 ::end # api-keys
88
89 ::node[id=__changelog type=meta]
90 ::changelog
91

2025-04-15|added
2025-04-10|updated
2025-03-01|deprecated|node[heroku-deploy]

|node[kubernetes-deploy]|New k8s support added
|node[install]

|--break-system-packages flag
|Heroku free tier ended

92

93
94 ::end
95 ::end # __changelog

12

