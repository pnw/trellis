---
title: "TagRAG: Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented Generation"
authors: "Wenbiao Tao, Xinyuan Li, Yunshi Lan, Weining Qian (East China Normal University)"
source: https://arxiv.org/abs/2601.05254
published: "2026-01-09"
venue: "ACL 2026 Findings"
retrieved: 2026-07-04
---

TagRAG: Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented
Generation

Wenbiao Tao, Xinyuan Li, Yunshi Lan*, Weining Qian
East China Normal University
{wbtao, xyli}@stu.ecnu.edu.cn, {yslan, wnqian}@dase.ecnu.edu.cn

6
2
0
2

y
a
M
2

]

R

I
.
s
c
[

3
v
4
5
2
5
0
.
1
0
6
2
:
v
i
X
r
a

Abstract

Retrieval-Augmented Generation enhances lan-
guage models by retrieving external knowl-
edge to support informed and grounded re-
sponses. However, traditional RAG methods
rely on fragment-level retrieval, limiting their
ability to address query-focused summariza-
tion queries. GraphRAG introduces a graph-
based paradigm for global knowledge reason-
ing, yet suffers from inefficiencies in informa-
tion extraction, costly resource consumption,
and poor adaptability to incremental updates.
To overcome these limitations, we propose
TagRAG, a tag-guided hierarchical knowledge
graph RAG framework designed for efficient
global reasoning and scalable graph mainte-
nance. TagRAG introduces two key compo-
nents: (1) Tag Knowledge Graph Construction,
which extracts object tags and their relation-
ships from documents and organizes them into
hierarchical domain tag chains for structured
knowledge representation, and (2) Tag-Guided
Retrieval-Augmented Generation, which re-
trieves domain-centric tag chains to localize
and synthesize relevant knowledge during in-
ference. This design significantly adapts to
smaller language models, improves retrieval
granularity, and supports efficient knowledge
increment. Extensive experiments on Ultra-
Domain datasets spanning Agriculture, Com-
puter Science, Law, and cross-domain settings
demonstrate that TagRAG achieves an average
winning rate of 78.36% against baselines while
maintaining about 14.6x construction and 1.9x
retrieval efficiency compared with GraphRAG.

1

Introduction

Retrieval-Augmented Generation (RAG) (Lewis
et al., 2020) is a framework that enhances the out-
put of language models by retrieving relevant doc-
uments from an external knowledge source and
conditioning the generation process on both the in-
put query and the retrieved content, enabling more

*Corresponding author

Figure 1: Inefficient graph construction and reasoning.

informed and factually grounded responses (Fan
et al., 2024; Chen et al., 2025b). For Large Lan-
guage Models (LLMs), RAG has become the most
important technology to help them land effec-
tively in the fields of medicine (Zhao et al., 2025),
law (Wiratunga et al., 2024), finance (Barry et al.,
2025), education (Lan et al., 2025), etc. However,
conventional RAG approaches typically rely on
unstructured text retrieval, which often fails to cap-
ture the intricate semantic relationships required
for complex reasoning (Liang et al., 2024), thereby
motivating the integration of graph-based question
answering (Tao et al., 2024) to better leverage struc-
tured knowledge (Zhu et al., 2025).

The emergence of GraphRAG (Edge et al., 2024)
solves this problem by extracting entities from doc-
uments, dividing knowledge communities, and gen-
erating community summaries, thereby refining
global information. The new paradigm of intro-
ducing knowledge summarization into RAG at the
graph level makes it realistic for LLMs to gen-
erate responses from a global view. However,
GraphRAG still suffers from the drawbacks of in-
efficient information extraction and expensive re-
source calls. To solve these problems, some meth-
ods, such as LightRAG (Guo et al., 2025) and KET-
RAG (Huang et al., 2025b), simplify the knowledge
graph structure, avoiding complicated community
divisions and reducing construction costs signifi-

Entity/RelationextractionCommunitysummarizationDocumentsKnowledgeGraphNewDocumentsEntity/RelationextractionDocumentsGraphKnowledgeKnowledgesummarizationNewDocumentsKnowledgesummarizationUserLLMQuestionsMergeAnswersRetrieveResponse：IncrementalKnowledgeInsertion：KnowledgeGraphConstruction：Retrieval-AugmentedGeneration 
 
 
 
 
 
cantly. Besides, for improving the efficiency of in-
ference, methods like MiniRAG (Fan et al., 2025),
FG-RAG (Hong et al., 2025) and LeanRAG (Zhang
et al., 2026) retrieve relevant subgraphs to generate
query-aware fine-grained answers. However, these
approaches are divorced from a global perspective.
Although it is possible to inject the intrinsic knowl-
edge of LLMs into the entity in the process of
building the graph, it is difficult to compensate for
the comprehensive understanding of the complete
resource library.

Based on the above issues, we revisit GraphRAG
and present the following two research questions.

• (RQ1) How to enhance the global knowl-
edge graph representation and reasoning
with low resource consumption? Existing
Graph RAG methods heavily rely on large-
scale LLMs (e.g., GPT-4o (Hurst et al., 2024))
to handle construction, retrieval, and gener-
ation, hindering migration to smaller mod-
els due to limited capacity. These high-
intensity model calls also incur substantial
resource costs and constrain deployment flexi-
bility. Therefore, decoupling LLMs’ end-to-
end dominance becomes essential for practical
and scalable applications.

• (RQ2) How to achieve robust and efficient
knowledge increment for large-scale Graph
RAG? GraphRAG employs a bottom-up con-
struction paradigm that involves entity/rela-
tionship extraction followed by community
summary generation. However, this architec-
ture struggles with incremental updates, re-
quiring costly full-graph reconstruction. Con-
sequently, it is crucial to develop an efficient
incremental construction mechanism that min-
imizes overhead and integrates seamlessly
with existing knowledge structures.

To tackle these challenges, we propose
TagRAG, a tag-guided hierarchical knowledge
graph retrieval-augmented generation framework,
comprising Tag Knowledge Graph Construction
and Tag-guided Retrieval-Augmented Generation.
In the construction stage, TagRAG constructs a
Tag Knowledge Graph by extracting object tag
keywords and their relationships from documents.
These object tags are linked to predefined root do-
main tags, forming hierarchical domain tag chains.
Knowledge from object tags connected to domain

tags is summarized and fused for information inte-
gration. During inference, domain-centric tags are
retrieved to localize knowledge. The hierarchical
tag chains are collected to integrate synthesized in-
formation, which is then fused into global answers
via tag-guided retrieval-augmented generation. In
summary, the contributions are as follows:

• We propose TagRAG, a powerful and efficient
graph-based RAG framework that enhances
global knowledge representation and reason-
ing in low-resource scenarios.

• We introduce the architecture of domain tag
chains, which improves the hierarchy of
knowledge graphs and optimizes the adapt-
ability of incremental insertion.

• We extensively evaluate our framework on
UltraDomain Agriculture, CS, Legal and Mix,
demonstrating its effectiveness and efficiency
for graph-based RAG.

2 Related Work

Graph-based RAG (Peng et al., 2024) builds graphs
characterized by high-level knowledge representa-
tions and generate responses through global search.
RAPTOR (Sarthi et al., 2024) introduces hierarchi-
cal tree structures via clustering and summarization,
shifting RAG from chunk-based retrieval to struc-
tured reasoning. GraphRAG (Edge et al., 2024)
further enriches this modeling with diverse graph
representations, followed by HiRAG (Huang et al.,
2025a) and ArchRAG (Wang et al., 2025), which
utilize hierarchical community summaries. How-
ever, the heavy reliance on frequent LLM calls and
extensive summarization makes GraphRAG pro-
hibitively expensive and inefficient for practical
deployment.

The subsequent work has been improved in the
following two aspects: (1)Structural simplifica-
tion for graph construction. LightRAG (Guo
et al., 2025) integrates lightweight graphs with
text indexing and dual-level retrieval for efficient,
adaptive knowledge access. KET-RAG (Huang
et al., 2025b) combines a sparse knowledge graph
skeleton with a text-keyword bipartite graph, en-
abling multi-granular retrieval without building a
full-scale graph. (2)Retrieval optimization for
global knowledge. MiniRAG (Fan et al., 2025)
unifies text and entity indexing into a semantic-
aware graph,
leveraging lightweight topology-
enhanced search for efficient knowledge access.

FG-RAG (Hong et al., 2025) extends entity cover-
age via context-aware graph retrieval and improves
response specificity with query-level fine-grained
summarization. PathRAG (Chen et al., 2025a) ex-
tracts key relational paths and converts them into
text prompts, guiding LLMs toward more coherent
and context-aware generation.

However, these approaches perform poorly in
low-resource scenarios where smaller LLMs are
deployed and are rarely explored on incremental
knowledge. TagRAG injects powerful retrieval
and reasoning capabilities into an efficiently con-
structed knowledge graph while supporting incre-
mental knowledge integration.

3 Task Definition

TagRAG is dedicated to building a hierarchically
explicit knowledge graph under any domain to
enable powerful and efficient RAG capabilities.
Given a set of documents D = {di}|D|
i=1, key do-
main information are extracted to construct an ob-
ject tag knowledge graph Go = (Vo, Eo). In order
to form a clear structured knowledge management,
given a root domain ˆv, a hierarchical domain tag
system Gd = (Vd, Ed) needs to be established. It
contains domain tags Vd at different levels and
hierarchical relationships Ed between tags. For
knowledge coordination and fusion, the object tags
should be linked to the domain tag system and a
hierarchical tag knowledge graph is constructed:

G = (Vo, Eo, Vd, Ed, Eod),

where Eod represents the relationships between the
object and domain tags.

For retrieval-augmented generation, given a
question q, the hierarchical tag knowledge graph is
searched to generate a global and comprehensive
answer a:

a ← F(q, G),

where F(·) means the graph-based RAG method.

4 TagRAG

As shown in Figure 2, TagRAG consists of two
stage: (1) Tag Knowledge Graph Construction and
(2) Tag-guided Retrieval-Augmented Generation.
We extract the keywords from documents as object
tags as well as their relationships. Linking them to
the pre-defined root domain tag, domain tag chains
are organized for knowledge accommodation. For

information integration, the knowledge from object
tags connected to domain tags is fused with sum-
marization. In the inference stage, domain-centric
tags are retrieved for knowledge localization. With
the hierarchical tag chains collected, more synthe-
sized information is integrated and can be fused to
the global answers.

4.1 Tag Knowledge Graph Construction

TagRAG aims to build a knowledge graph with
rich domain relationships and efficiently aggregates
global knowledge. We extract object tag keywords
to collect expertise, organize domain tag chains
to build a hierarchical structured system, and fuse
domain-centric knowledge summaries to provide
an efficient retrieval platform.

4.1.1 Object Tag Keyword Extraction

In order to accurately access the knowledge in the
corpus, we need to refine specialized domain doc-
uments. Following the RAG paradigm, the set of
documents D = {di}|D|
i=1 are divided into several
chunks T = {ti}|T |
i=1 with overlaps to reach the
size that LLMs can handle and maintain seman-
tic coherence. Then, we request LLMs to extract
domain-specific keywords with their descriptions
as object tags:

Vo, Eo = LLM({ti}|T |

i=1),

which contain the most primitive and underlying
information in the document.

4.1.2 Domain Tag Chain Organization

The extracted object tags are scattered nodes that
are difficult to manage hierarchically. Unlike the
bottom-up construction of GraphRAG, we asso-
ciate them with the predefined root domain tag.
This gives the whole construction process a clear
sense of direction and satisfies the specialized na-
ture of domain knowledge graphs. Specifically,
given object tags with the predefined root domain
tag, we prompt LLMs to generate relationships
between them and abstract them into multi-level
domain tag chains:

C = {ci}|Vo|

i=1 = LLM(Vo.ˆv),

Each ci contains multiple domain tags, each con-
sisting of a domain name and its description. Supe-
rior domain tag points to the subordinate domain
tag through the relationship of "has subdomain".

Figure 2: The proposed TagRAG framework.

These domain tag chains, featuring explicit
pointing relationships, inherently carry the hier-
archical knowledge logic from general categories
to specific subfields. To consolidate this logic into
a structured framework that avoids redundant as-
sociations and cyclic dependencies, we merge the
chains into a directed acyclic graph (DAG) that
clearly embodies the layered hierarchy of domain
knowledge while ensuring intuitive traversal be-
tween different levels of tags. Starting at the head
of the chain, each node is mounted at its parent’s
corresponding position in the DAG to ensure the
integrity of the chain and the transitivity of the
DAG. The detailed process of domain tag chain
organization can be seen in Algorithm 1.

4.1.3 Domain-centric Knowledge Fusion

In order to efficiently retrieve domain information,
we deploy knowledge fusion in the graph construc-
tion phase in advance, which aggregates all highly
relevant information into domain tags. Specifically,
there are two such categories of information:

• Domain information on chains: there are
multiple domain nodes on domain tag chains
that contain rich high-level domain informa-
tion. They are natural providers of compre-
hensive field vision.

Algorithm 1: Domain Tag Chain Organiza-
tion
1 Input: The list of domain tag chain C, the
root domain tag ˆv and the existing
tag knowledge graph G.

2 Output: ˆG.
3 DAG ← {ˆv};
4 foreach ci ∈ C do
5

for j from 2 to |ci| − 1 do

6

7

8

9

10

11

12

13

14

pi,j ← get_node(DAG, ci,j−1);
ni,j ← get_node(DAG, ci,j);
if pi,j is not None then

if ni,j is not None then

if ni,j /∈ pi,j.children then
pi,j.add_child(ni,j);

else

nnew ← new_node(ci,j);
pi,j.add_child(nnew);

15 ˆG ← merge_graph(G, DAG);
16 return ˆG

original documents. They can provide accu-
rate grounding knowledge.

Combining these two aspects of data, we fused
them into the domain-centric knowledge summary:

• Specialized knowledge in objects: the ex-
tracted object tags contain the expertise in the

s = LLM(Chain(vd), Nei(vd)),

......Object Tag Keyword ExtractionDomain Tag Chain OrganizationDoc1:Doc1:Apache Spark is a new framework for distributed computing that is designed from the groundup tobe optimized for.........DomainTagsObjectTags......DomainTagsObjectTagsDomain-centric KnowledgeDomainTag:BigDataObjectTags:[Apache Spark,...,HDFS]Chain:ComputerScience–>DataProcessing–>...–>BigDataSummary:The domain encompasses the study and application of computational systems and algorithms, with a focus on solving complex problems through software and hardware. At its core lies **Computer Science**, ...Domain-centric Knowledge FusionQuestion:How does Spark Streaming enable real-time data processing?Tag-guided Retrieval-Augmented GenerationTag Knowledge Graph ConstructionSpark ClustersSpark ContextSpark ShellRDDCountSumLineOnline StoreCSV FileProductUserSpark APPDecision TreeData SourcesRDDSparkDistributed ComputingComputerScienceComputerScienceComputerScienceComputerScienceDecision TreeMachine LearningText GenerationEmpty SetFormal SystemsRandom VariableProbability and StatisticsName:ComputerScienceDescription:Computer Science is the study of computational systems ...DomainDocumentsName:Apache SparkDescription:Adistributed computing system designed ...low-latency tasks.KGTag Knowledge-Fused GenerationHierarchical Tag Chain IntegrationDomain-centric Knowledge RetrievalAnswer: Spark Streaming extends the core Spark ...where vd ∈ Vd denotes each domain tag, Chain(·)
indicates the domain tag chain to which vd belongs,
and Nei(·) represents the object tags linked to vd.
Embedded in the summary, each domain tag is
accompanied by global knowledge related to itself.
After vectorizing these summaries, we obtain a
diverse and global domain-centric knowledge re-
trieval library:

K ← {vi, si, Emb(si)}|Vd|
i=1,

where Emb(·) is the embedding function, vi and si
denote a domain tag and its summary, respectively.

4.1.4 Knowledge Incremental Insertion
The TagRAG framework has a natural advantage
in knowledge incremental insertion. Instead of di-
viding communities from scratch, TagRAG can di-
rectly embed newly constructed domain tag chains
into the existing knowledge graph. The incremental
process involves two components:

• Tag increment: For the new extracted object
tags or generated domain tags, TagRAG ap-
pends new descriptions to the existing ones
with the same name.

• Knowledge increment: For the new fused
domain-centric knowledge, TagRAG re-
summarizes old and new summaries of do-
main tags with the same name to generate
new perceptions.

Compared to the time-consuming full reconstruc-
tion of GraphRAG, TagRAG’s incremental inser-
tion mechanism is significantly more efficient.

4.2 Tag-guided Retrieval-Augmented

Generation

Following the global vision strategy, TagRAG uses
tag-guided graph retrieval-augmented generation.
As the existence of domain tags that carry global
knowledge, TagRAG is more efficient than other
summarization-based and walk-based methods.

4.2.1 Domain-centric Knowledge Retrieval
Based on the domain-centric knowledge retrieval
library, we can search domain knowledge related
to the question:

′

′

(V

t , S

t) = Rettag(q, K),

where V ′
t indicates the related domain tags, S ′
t rep-
resents the related summaries, and Rettag(·) is the
retrieval function with cosine similarity.

4.2.2 Hierarchical Tag Chain Integration
Thanks to knowledge fusion, domain-centric
knowledge already has global properties. How-
ever, with the advantage of hierarchical knowledge
graph, we are able to further extract higher-level
global knowledge:

′

′

(V

c , S

c) = Retchain(V

′

t ),

where Retchain(·) extracts the corresponding chains,
V ′
c indicates the domain tags on the chain corre-
t , and S ′
sponding to V ′
c represents the summaries
implied by V ′
c .

4.2.3 Tag Knowledge-Fused Generation
With the retrieved summaries, global information is
achieved for response generation. Constrained by
the input length of the LLMs, we prioritize putting
in the related domain tag summaries S ′
t, and then
adding the related chain summaries S ′
c until the
upper limit is reached. Given the question and
the domain knowledge summaries, the answer is
generated by the LLM:

a = LLM(q, S

′

′

t, S

c).

4.3 Analysis of Retrieval Complexity

GraphRAG’s inefficiency stems from its multi-
stage pipeline, requiring extensive LLM calls for
entity extraction and community detection (e.g.,
Leiden algorithm), leading to high computational
costs and frequent full graph reconstructions for
dynamic data. In contrast, TagRAG’s domain tag
chains enable hierarchical information aggrega-
tion during graph building, replacing iterative com-
munity partitioning with linear chain processing.
During inference, TagRAG utilizes vector match-
ing and tag chain linking, avoiding GraphRAG’s
costly full graph traversal. Both stages demonstrate
TagRAG’s superior efficiency over GraphRAG.

5 Experimental Setup

5.1 Datasets and Baselines

To demonstrate the high applicability of TagRAG,
following standard evaluation on Graph-based
RAG methods (Edge et al., 2024; Guo et al., 2025;
Chen et al., 2025a), we chose four corpus from
the comprehensive UltraDomain (Qian et al., 2025)
benchmark, Agriculture, CS, Legal and Mix. Fol-
lowing LightRAG, we used GPT-4o-mini to gener-
ate 125 global questions for each dataset, covering
different domains and different tasks. The dataset

details and question generation prompt can be seen
in Appendix A.2 and C.

To validate the performance and efficiency of
global question answering, we compare TagRAG
with two types of baselines. (1) Zero-shot LLM
Generation: We call Qwen3-4B (Team, 2025),
Qwen3-30B-A3B (Team, 2025) and Llama-3.3-
70B-Instruct (Grattafiori et al., 2024) to directly
answer the questions. (2) Retrieval-Augmented
Generation: NaiveRAG (Lewis et al., 2020) fo-
cuses on local context through dynamic document
retrieval. GraphRAG (Edge et al., 2024) utilizes
entity graphs and community summaries for global
knowledge synthesis. LightRAG (Guo et al., 2025)
is a lightweight baseline that integrates graph struc-
tures with dual-level text indexing for fast and
real-time updates. MiniRAG (Fan et al., 2025)
achieves high efficiency on small language models
via semantic-aware graph indexing and lightweight
topology-based retrieval. Detailed descriptions are
shown in Appendix A.3.

5.2 Evaluation Metrics

Four evaluation metrics were used to assess the
performance of the comparison methods: Com-
prehensiveness: How much detail does the an-
swer provide to cover all aspects and details of the
question? Diversity: How varied and rich is the
answer in providing different perspectives and in-
sights on the question? Empowerment: How well
does the answer help the reader understand and
make informed judgments about the topic? Over-
all: Which answer is better overall?

We utilize the powerful model GPT-4o-mini,
gemini-2.5-pro and claude-sonnet-4.5-20250929
to determine the winner for each of the two com-
parison methods based on the above metrics. For
each dataset, we also exchange the order of the
results of the two comparison methods to avoid po-
sition bias. Finally, we report the average of 3*2=6
evaluation results. The evaluation prompt can be
seen in Appendix C.

5.3

Implementation Details

Agri CS

Legal Mix Avg

Zero-shot LLM Generation

v.s. Qwen3-4B

Comprehensiveness
Diversity
Empowerment
Overall

85.9
78.9
80.7
83.2

69.6
64.4
57.5
59.3

70.3
62.0
48.9
53.7

v.s. Qwen3-30B-A3B

Comprehensiveness
Diversity
Empowerment
Overall

84.8
79.5
76.4
80.3

68.8
65.1
53.2
55.5

72.7
62.1
45.6
51.6

v.s. Llama-3.3-70B-Instruct

Comprehensiveness
Diversity
Empowerment
Overall

68.1
67.5
56.9
65.9

51.5
58.5
43.1
49.3

49.7
43.1
27.2
39.7

58.8
53.9
45.7
49.3

59.6
59.6
40.4
44.7

27.7
35.9
22.8
27.3

Retrieval-Augmented Generation

v.s. NaiveRAG

Comprehensiveness
Diversity
Empowerment
Overall

93.9
90.4
91.2
93.5

94.0
95.5
88.3
89.7

v.s. GraphRAG

Comprehensiveness
Diversity
Empowerment
Overall

89.3
88.5
90.8
90.9

85.3
85.5
81.6
81.9

v.s. LightRAG

Comprehensiveness
Diversity
Empowerment
Overall

94.4
94.9
95.5
94.4

85.1
88.1
85.7
84.0

v.s. MiniRAG

Comprehensiveness
Diversity
Empowerment
Overall

76.0
80.7
79.1
78.3

55.2
64.7
59.7
58.4

79.5
95.2
74.9
72.3

60.7
72.0
63.2
62.3

80.3
88.5
82.0
79.9

56.8
70.4
59.5
57.5

90.0
95.2
88.1
87.9

67.1
74.9
67.9
67.7

88.1
92.3
91.6
89.7

64.1
77.1
67.3
65.3

71.2
64.8
58.2
61.4

71.5
66.6
53.9
58.0

49.2
51.2
37.5
45.5

89.3
94.1
85.6
85.8

75.6
80.2
75.9
75.7

87.0
91.0
88.7
87.0

63.0
73.2
66.4
64.9

Table 1: Main results: winning rates (%) of TagRAG
v.s. baselines with Qwen3-4B across four datasets.

vectordb 1. The top-k number for Domain-centric
Knowledge Retrieval is 3. More detailed experi-
mental settings can be found in Appendix A.

6 Results and Analysis

6.1 Main Results

We use Qwen3-4B (Team, 2025) as the backbone
to conduct the experiments without thinking. bge-
large-en-v1.5 (Xiao et al., 2023) is employed to
embed questions and documents. The chunk size
and overlap size are 1200 and 100, respectively.
The vector database used in this work is nano-

Table 1 evaluates the winning rate of TagRAG
against NaiveRAG, GraphRAG, LightRAG, and
MiniRAG on four datasets: UltraDomain Agri-
culture, CS, Legal, and Mix. We can draw the

1https://github.com/gusye1234/nano-vectordb

(a) On UltraDomain Agriculture

(b) On UltraDomain CS

(c) On UltraDomain Legal

(d) On UltraDomain Mix

Figure 3: Performance-efficiency analysis: comparative winning rates, graph construction time and inference time
results of TagRAG and baselines across four datasets. The larger the bubble and the closer to the lower left corner,
the better the method.

following conclusions: (1)TagRAG leads in per-
formance, achieving an average winning per-
centage of 82.85% compared with NaiveRAG,
GraphRAG, and LightRAG. Even against Mini-
RAG, the strongest baseline, TagRAG maintains
a dominant average winning rate, with MiniRAG
retaining only 35.125%. (2)TagRAG excels at Di-
versity, leveraging its domain knowledge integra-
tion to access broader information for generation.
Even when compared to GraphRAG, which tra-
verses all communities, TagRAG maintains a clear
advantage, suggesting that fusing knowledge via
domain chains is superior to community-summary
(3)TagRAG ex-
or path-discovery approaches.
pands the model capability, because it defeats
the LLM with 7 times the parameters by virtue of
the fused domain chain information. Even facing
the 70B model, TagRAG can compete with it. This
demonstrates that TagRAG does not rely solely on
the inherent capabilities of the language model, and
that the tag chain mechanism effectively broadens
the boundaries of global reasoning.

6.2 Performance-efficiency Analysis

In Figure 3, we show the performance, graph con-
struction time and inference time of different meth-
ods. TagRAG, which presents the largest bubbles,
embodies the strongest performance, and possesses
low graph construction time and inference time.
GraphRAG not only exhibits weak performance,
but also consumes extremely high construction and

Agri

CS

Legal Mix

v.s. w/o chain

Comprehensiveness
Diversity
Empowerment
Overall

87.1
84.7
86.8
87.2

90.5
87.3
84.5
87.5

v.s. w/o fusion

Comprehensiveness
Diversity
Empowerment
Overall

97.3
96.4
96.9
96.9

95.5
94.1
87.1
89.7

85.2
85.6
77.7
80.1

95.5
94.5
85.1
88.0

78.9
76.3
72.8
75.2

85.9
89.1
76.9
78.4

Table 2: Ablation study: winning rates (%) of TagRAG
v.s. w/o chain and w/o fusion with Qwen3-4B across
four datasets.

inference costs. MiniRAG has the next strongest
performance, but its graph construction time is far
behind TagRAG, due to its ultimate entity and re-
lationship extraction. Despite the excellent time
overhead with lightweight extraction, the perfor-
mance of LightRAG is the worst, subject to the gap
of high and low level semantics. Taken together,
thanks to the advanced domain chain indexing and
knowledge integration, TagRAG has achieved the
strongest performance-efficiency results.

6.3 Ablation Study

We conduct ablation experiments on the four
datasets by comparing TagRAG with TagRAG w/o
chain and w/o fusion. TagRAG w/o chain simply
adds the retrieved fused domain-centric knowledge

255075100125150175200225Graph Construction Time (Hours)01020304050Inference Time (Hours)TagRAGGraphRAGLightRAGMiniRAG020406080100Win Rate (%)406080100120140160180Graph Construction Time (Hours)05101520253035Inference Time (Hours)TagRAGGraphRAGLightRAGMiniRAG020406080100Win Rate (%)100150200250300350Graph Construction Time (Hours)01020304050Inference Time (Hours)TagRAGGraphRAGLightRAGMiniRAG020406080100Win Rate (%)10203040506070Graph Construction Time (Hours)010203040Inference Time (Hours)TagRAGGraphRAGLightRAGMiniRAG020406080100Win Rate (%)(a) Comprehensiveness

(b) Diversity

(c) Empowerment

(d) Overall

Figure 4: Incremental analysis: winning rates (%) of TagRAG v.s. baselines with Qwen3-4B across four datasets in
10 rounds. The red horizontal line represents equilibrium and values above it indicate TagRAG’s advantage.

v.s. NaiveRAG

v.s. GraphRAG

v.s. LightRAG

v.s. MiniRAG

large

base

small

large

base

small

large

base

small

large

base

small

Comprehensiveness
Diversity
Empowerment
Overall

94.0
95.5
88.3
89.7

93.7
95.6
90.9
89.9

93.1
96.3
90.5
91.1

85.3
85.5
81.6
81.9

86.0
85.6
84.4
82.8

86.1
87.2
85.2
85.1

85.1
88.1
85.7
84.0

81.5
87.3
84.9
82.5

82.3
86.8
85.7
83.3

55.2
64.7
59.7
58.4

57.5
69.2
62.8
60.7

59.9
66.0
64.5
62.8

Table 3: Retriever adaption analysis: winning rates (%) of TagRAG v.s. baselines with Qwen3-4B on CS, equiped
with different retrievers of bge-large-en-v1.5, bge-base-en-v1.5 and bge-small-en-v1.5.

to the context without involving the information in
the associated domain chain. And TagRAG w/o fu-
sion not only discards the knowledge of the domain
chain, but also cuts off the object tag information
connected to the retrieved domain tag. It relies
entirely on the description of the domain tags to
answer the question. It can be clearly found that
(1) the absence of these two components makes
the answers generated by the model far inferior to
the full TagRAG and (2) retaining fused domain-
centric knowledge is better than simply using the
description of domain tags for generation.

6.4

Incremental Analysis

To validate that our proposed method can accom-
modate incremental scenarios, we incrementally
construct a knowledge graph from 10 documents in
the UltraDomain CS dataset. After each round of
increment, we generate diverse questions involving
all current documents to test the global reasoning
capabilities of different methods. In Figure 4, Tag
RAG has a steady lead over Naive RAG, Graph
RAG and Light RAG, with average winning rates
reaching over 80%. Even though there is a close tie

with TagRAG in the first round, MiniRAG loses as
the documents increase. This proves that TagRAG
has a stable global inference capability in incremen-
tal scenarios with multiple rounds, as the mecha-
nism of tag chain fusion naturally has the advantage
of infinite scaling.

6.5 Retriever adaption analysis

To demonstrate that our performance does not
solely depend on the effect of a powerful searcher,
we perform a retriever adaption analysis. As shown
in Table 3, retrievers of different sizes are applied
to the comparison. Even with a lower performance
retriever, TagRAG still has a stable advantage in all
metrics. Even in comparison with GraphRAG, the
poorer retriever excites the potential of TagRAG.
This suggests that domain clustering in the form of
tag chains based on DAG weakens the need for pre-
cise entity retrieval and enhances the representation
of global knowledge.

6.6 Cross-domain incremental analysis

To demonstrate cross-domain capabilities, we add
a document from the UltraDomain CS dataset to

12345678910Round405060708090100Winning Rate (%)v.s. NaiveRAGv.s. GraphRAGv.s. LightRAGv.s. MiniRAG12345678910Round405060708090100Winning Rate (%)v.s. NaiveRAGv.s. GraphRAGv.s. LightRAGv.s. MiniRAG12345678910Round405060708090100Winning Rate (%)v.s. NaiveRAGv.s. GraphRAGv.s. LightRAGv.s. MiniRAG12345678910Round405060708090100Winning Rate (%)v.s. NaiveRAGv.s. GraphRAGv.s. LightRAGv.s. MiniRAGComprehensiveness Diversity

Empowerment Overall

Time-C Time-I

GraphRAG
LightRAG
MiniRAG
TagRAG

41.7
53.5
53.9
56.1

42.8
54.5
53.2
56.1

43.2
52.9
52.9
56.8

44.0
52.9
54.1
58.0

30.47
2.28
9.83
6.37

36.81
4.01
8.80
2.47

Table 4: Cross-domain incremental analysis: winning rates(%) of results after v.s. before upserting. Time-C (hours)
and Time-I (hours) denote incremental graph construction time and inference time, respectively.

the Mix-built knowledge graph. After integra-
tion, we evaluate whether comparative methods can
leverage this incremental knowledge to improve re-
sponses to Mix-generated questions. As shown
in Table 4, TagRAG substantially outperforms the
other methods in performance while achieving sub-
optimal time results. LightRAG, despite its time
advantage, is limited by polarized knowledge rep-
resentation, hindering effective merging into the
existing framework and leading to unsatisfactory
incremental performance. GraphRAG consumes
the most time due to numerous LLM calls and com-
munity summarizations, struggling to incorporate
entirely new domains into established communities,
resulting in poor performance.

6.7 Visualization of Knowledge Graph

Construction

To distinguish the methods, we visualize their
knowledge graphs on UltraDomain Mix in Fig-
ure 5. Without a strong semantic parser, Ligh-
tRAG with a smaller model extracts sparse enti-
ties and loose relations, resulting in low-density
graphs. GraphRAG and MiniRAG produce similar
graphs. While GraphRAG adds global knowledge
via community summaries, MiniRAG is more ef-
fective on small models through tailored retrieval.
Leveraging hierarchical links, TagRAG builds well-
connected graphs with high knowledge density and
broad coverage.

7 Conclusion

We propose TagRAG, a tag-guided hierarchical
knowledge graph RAG framework that addresses
key limitations of existing graph-based RAG sys-
tems, such as inefficient global reasoning and poor
increment adaptability. By constructing domain-
aware tag chains and enabling tag-guided graph re-
trieval, TagRAG achieves structured, fine-grained,
and scalable knowledge integration. Our design
reduces reliance on large language models and sup-
ports efficient construction and inference. The ex-
perimental results on the UltraDomain benchmark

(a) GraphRAG

(b) LightRAG

(c) MiniRAG

(d) TagRAG

Figure 5: Visualization of knowledge graph construction
with Qwen3-4B on UltraDomain Mix.

show that TagRAG achieves a 78.36% average win-
ning rate over baselines while offering significant
gains in construction (14.6×) and retrieval (1.9×)
efficiency compared to GraphRAG.

Limitations

The indexing pipeline of TagRAG depends on LLM
calls for object tag extraction and domain chain
construction, which raises questions about cost, re-
producibility, and robustness in fully automated
scenarios. In addition, TagRAG cannot handle mul-
timedia data such as pictures and videos, which
limits its application scope.

Acknowledgments

The authors would like to thank the anonymous
reviewers for their insightful comments. This
work is supported by the National Key Research
& Develop Plan (Project No.2023YFF0725100)
and Natural Science Foundation of China (Project
No.U23A20298).

References

Mariam Barry, Gaëtan Caillaut, Pierre Halftermeyer, Ra-
heel Qader, Mehdi Mouayad, Dimitri Cariolaro, Fab-
rice Le Deit, and Joseph Gesnouin. 2025. Graphrag:
leveraging graph-based efficiency to minimize hallu-
cinations in llm-driven rag for finance data. In 31st
International conference on Computational Linguis-
tics Workshop Knowledge Graph & GenAI.

Boyu Chen, Zirui Guo, Zidan Yang, Yuluo Chen, Junze
Chen, Zhenghao Liu, Chuan Shi, and Cheng Yang.
2025a. Pathrag: Pruning graph-based retrieval aug-
arXiv
mented generation with relational paths.
preprint arXiv:2502.14902.

Qinwen Chen, Wenbiao Tao, Zhiwei Zhu, Mingfan Xi,
Liangzhong Guo, Yuan Wang, Wei Wang, and Yunshi
Lan. 2025b. Comrag: Retrieval-augmented genera-
tion with dynamic vector stores for real-time com-
munity question answering in industry. In Proceed-
ings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 6: Industry
Track), pages 749–763.

Darren Edge, Ha Trinh, Newman Cheng, Joshua
Bradley, Alex Chao, Apurva Mody, Steven Truitt,
Dasha Metropolitansky, Robert Osazuwa Ness, and
Jonathan Larson. 2024. From local to global: A
graph rag approach to query-focused summarization.
arXiv preprint arXiv:2404.16130.

Tianyu Fan, Jingyuan Wang, Xubin Ren, and Chao
Huang. 2025. Minirag: Towards extremely sim-
ple retrieval-augmented generation. arXiv preprint
arXiv:2501.06713.

Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang,
Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing
Li. 2024. A survey on rag meeting llms: Towards
retrieval-augmented large language models. In Pro-
ceedings of the 30th ACM SIGKDD conference on
knowledge discovery and data mining, pages 6491–
6501.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.

Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, and Chao
Huang. 2025. LightRAG: Simple and fast retrieval-
augmented generation. In Findings of the Association
for Computational Linguistics: EMNLP 2025, pages
10746–10761.

Yubin Hong, Chaofan Li, Jingyi Zhang, and Yingxia
Shao. 2025. Fg-rag: Enhancing query-focused sum-
marization with context-aware fine-grained graph rag.
arXiv preprint arXiv:2504.07103.

Haoyu Huang, Yongfeng Huang, Junjie Yang, Zhenyu
Pan, Yongqiang Chen, Kaili Ma, Hongzhi Chen, and
James Cheng. 2025a. Retrieval-augmented gener-
ation with hierarchical knowledge. arXiv preprint
arXiv:2503.10150.

Yiqian Huang, Shiqi Zhang, and Xiaokui Xiao. 2025b.
Ket-rag: A cost-efficient multi-granular index-
arXiv preprint
ing framework for graph-rag.
arXiv:2502.09304.

Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow,
Akila Welihinda, Alan Hayes, Alec Radford, and 1
others. 2024. Gpt-4o system card. arXiv preprint
arXiv:2410.21276.

Yunshi Lan, Xinyuan Li, Hanyue Du, Xuesong Lu,
Ming Gao, Weining Qian, and Aoying Zhou. 2025.
Survey of natural language processing for educa-
tion: Taxonomy, systematic review, and future trends.
IEEE Transactions on Knowledge and Data Engi-
neering.

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
rich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, and 1 others. 2020. Retrieval-augmented gen-
eration for knowledge-intensive nlp tasks. Advances
in neural information processing systems, 33:9459–
9474.

Yuanyuan Liang, Keren Tan, Tingyu Xie, Wenbiao Tao,
Siyuan Wang, Yunshi Lan, and Weining Qian. 2024.
Aligning large language models to a domain-specific
graph database for nl2gql. In Proceedings of the 33rd
ACM international conference on information and
knowledge management, pages 1367–1377.

Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo,
Haizhou Shi, Chuntao Hong, Yan Zhang, and Siliang
Tang. 2024. Graph retrieval-augmented generation:
A survey. arXiv preprint arXiv:2408.08921.

Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao,
Defu Lian, Zhicheng Dou, and Tiejun Huang. 2025.
Memorag: Boosting long context processing with
global memory-enhanced retrieval augmentation. In
Proceedings of the ACM on Web Conference 2025,
pages 2366–2377.

Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh
Khanna, Anna Goldie, and Christopher D Manning.
2024. Raptor: Recursive abstractive processing for
tree-organized retrieval. In The Twelfth International
Conference on Learning Representations.

Wenbiao Tao, Hanlun Zhu, Keren Tan, Jiani Wang,
Yuanyuan Liang, Huihui Jiang, Pengcheng Yuan, and
Yunshi Lan. 2024. Finqa: A training-free dynamic
knowledge graph question answering system in fi-
nance with llm-based revision. In Joint European
Conference on Machine Learning and Knowledge
Discovery in Databases, pages 418–423. Springer.

Qwen Team. 2025. Qwen3 technical report. Preprint,

arXiv:2505.09388.

Shu Wang, Yixiang Fang, Yingli Zhou, Xilin Liu, and
Yuchi Ma. 2025. Archrag: Attributed community-
based hierarchical retrieval-augmented generation.
arXiv preprint arXiv:2502.09891.

Nirmalie Wiratunga, Ramitha Abeyratne, Lasal Jayawar-
dena, Kyle Martin, Stewart Massie, Ikechukwu Nkisi-
Orji, Ruvan Weerasinghe, Anne Liret, and Bruno
Fleisch. 2024. Cbr-rag: case-based reasoning for
retrieval augmented generation in llms for legal ques-
tion answering. In International Conference on Case-
Based Reasoning, pages 445–460. Springer.

Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas
Muennighoff. 2023. C-pack: Packaged resources
to advance general chinese embedding. Preprint,
arXiv:2309.07597.

Yaoze Zhang, Rong Wu, Pinlong Cai, Xiaoman Wang,
Guohang Yan, Song Mao, Ding Wang, and Botian
Shi. 2026. Leanrag: Knowledge-graph-based gen-
eration with semantic aggregation and hierarchical
retrieval. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pages 34862–
34869.

Xuejiao Zhao, Siyan Liu, Su-Yin Yang, and Chun-
yan Miao. 2025. Medrag: Enhancing retrieval-
augmented generation with knowledge graph-elicited
reasoning for healthcare copilot. In Proceedings of
the ACM on Web Conference 2025, pages 4442–4457.

Zulun Zhu, Tiancheng Huang, Kai Wang, Junda Ye,
Xinghe Chen, and Siqiang Luo. 2025. Graph-based
approaches and functionalities in retrieval-augmented
generation: A comprehensive survey. ACM Comput-
ing Surveys.

A Detailed Experimental Settings

A.1 Experimental Environment

In Table 5, we list the relevant experimental envi-
ronment information, including hardware and soft-
ware.

Configuration

CPU

Intel(R) Xeon(R) Gold 6330 CPU
@ 2.00GHz
NVIDIA RTX A6000 48GB
256GB

GPU
RAM
Operating System CentOS Linux 7
CUDA
Python

12.4
3.10.16

Table 5: Experimental environment.

A.2 Dataset Details

We conduct experiments on four datasets, namely
Agriculture, CS, Legal and Mix. Agriculture, CS
and Legal describe expertise in their respective
fields, while Mix mixes knowledge from 18 fields.
As shown in Table 6, the Agriculture and CS
datasets are comparable in size, with Legal being
the largest and Mix being the smallest.

Agri

CS

Legal

Mix

Docs
Chunks
Tokens
Size

12
1756
2,017,886
8.56MB

10
1858
2,306,535
8.51MB

61
94
579
4294
5,081,069
619,009
21.24MB 2.54MB

Table 6: Dataset details.

A.3 Baselines

To validate the performance and efficiency of
global question answering, we compare TagRAG
with the raw generation of three LLMs with dif-
ferent parameter amounts and the following four
RAG-based methods:

• NaiveRAG (Lewis et al., 2020): NaiveRAG,
focusing on local
information, combines
LLMs with external knowledge retrieval to
enhance response accuracy and relevance by
dynamically fetching context from databases
or documents before generating answers.

• GraphRAG (Edge et al., 2024): GraphRAG
builds an entity graph with community sum-
maries, retrieving and aggregating partial sum-
mary responses into final answers. It grasps a

complete global view and is capable of gener-
ating synthesized responses.

• LightRAG (Guo et al., 2025): LightRAG
combines graph structures with text indexing
for dual-level retrieval, enabling fast, relevant
knowledge access and real-time updates in
dynamic environments. It is compared as a
representative of lightweight.

• MiniRAG (Fan et al., 2025): MiniRAG is an
efficient RAG system using semantic-aware
graph indexing and lightweight topology-
based retrieval for effective knowledge dis-
covery with minimal semantic processing. As
a comparison, it has excellent Graph-based
RAG performance with small language mod-
els.

A.4 Predefined Root Domain Tag Details

In Table 7, we list the root domains with their de-
scriptions for the Domain Tag Chain Organization
on the UltraDomain datasets.

Domain Description

Agri

CS

Legal

Mix

Agriculture: Agriculture is the culti-
vation of crops and rearing of animals
for food, fiber, and other products to
sustain human life.
Computer Science: Computer Science
is the study of computational systems
and algorithms, focusing on design-
ing, analyzing, and applying software
and hardware to solve complex prob-
lems.
Legal: Legal refers to anything per-
taining to law, its principles, regula-
tions, or the formal administration of
justice within a society.
All disciplines: All disciplines refers
to the complete range of academic,
professional, and practical fields of
study, encompassing the humanities,
sciences, arts, social sciences, tech-
nologies, and applied domains that
collectively constitute human knowl-
edge and activity.

Table 7: Root domains with their descriptions.

B Extended experiments

B.1 Performance Analysis with
glm-edge-1.5b-chat

In order to verify the sensitivity of different meth-
ods to LLMs, we conducted further tests based
on glm-edge-1.5b-chat 2. As seen in Table 8,
GraphRAG, LightRAG and MiniRAG, that per-
form quite well with qwen3-4b, exhibit catas-
trophic global reasoning. This is due to the fact that
both community summarization and path inference
rely heavily on the capabilities of LLMs, causing
these methods to perform poorly with lightweight
models. On the contrary, in this low resource sit-
uation, NaiveRAG still retains basic reasoning ca-
pabilities. It can be seen that TagRAG can adapt
to large language models with different parameter
quantities and always has strong global reasoning
capabilities.

Agri CS

Legal Mix Avg

v.s. NaiveRAG

Comprehensiveness
Diversity
Empowerment
Overall

56.8
57.5
64.8
60.8

73.3
76.4
72.5
72.9

v.s. GraphRAG

Comprehensiveness
Diversity
Empowerment
Overall

100.0 98.1
100.0 98.3
98.5
99.9
98.3
99.9

v.s. LightRAG

Comprehensiveness
Diversity
Empowerment
Overall

100.0 99.2
100.0 99.6
100.0 99.2
100.0 99.2

v.s. MiniRAG

Comprehensiveness
Diversity
Empowerment
Overall

99.7
98.3
99.6
99.7

99.2
99.2
99.2
99.2

63.7
74.8
64.7
60.0

96.9
97.3
96.3
96.0

96.7
97.6
96.7
97.1

94.9
96.0
94.7
94.7

53.3
52.0
54.8
54.3

78.1
79.2
78.1
78.3

82.9
84.1
80.5
82.1

79.7
82.1
79.2
79.7

61.8
65.2
64.2
62.0

93.3
93.7
93.2
93.1

94.7
95.3
94.1
94.6

93.4
93.9
93.2
93.3

Table 8: Main results: winning rates (%) of TagRAG v.s.
baselines with glm-edge-1.5b-chat across four datasets.

B.2 Lightweight Adaption Analysis

To illustrate the suitability and advantages of
TagRAG on smaller LLMs, we use Qwen3-1.7B
as a backbone for knowledge graph construction
and inference, and compare it with other methods
with Qwen3-4B in Table 9. Even with a 57.5%

Comprehensiveness
Diversity
Empowerment
Overall

v.s. GraphRAG

68.5
68.7
66.5
67.7

Table 9: Lightweight adaption analysis: winning rates
(%) of TagRAG with Qwen3-1.7B v.s. GraphRAG with
Qwen3-4B on CS.

smaller LLM size, TagRAG absolutely dominates
over NaiveRAG, GraphRAG and LightRAG and
has comparable results to MiniRAG. This suggests
that the connection of domain chains and the fu-
sion of domain-centric knowledge can be adapted
to low-resource scenarios. TagRAG liberates the
dependence on LLMs for graph construction.

B.3 Semantic Inheritance Analysis

To validate the effectiveness of the DAG-based do-
main tag chains in aggregating entity semantics and
relationships, we conducted quantitative analyses
on information retention and semantic inheritance.
First, to evaluate whether entity information
propagates to higher levels, we calculated the co-
sine similarity between object tag descriptions and
their upper-level domain tag summaries across dif-
ferent depths. As shown in Table 10, the aver-
age cosine similarity starts at 0.6823 for Level 1
and gradually converges to approximately 0.5 after
Level 4. This indicates that domain tags closer to
the objects retain more specific information, while
higher-level tags effectively preserve a significant
portion of the entity semantics, facilitating seman-
tic clustering within the hierarchy.

Level Cosine Sim Avg

1
2
3
4
5
6
7
8
9

0.6823
0.5806
0.5305
0.4968
0.4919
0.4927
0.4980
0.5092
0.5166

Table 10: Cosine similarity for information propagation

2https://huggingface.co/zai-org/glm-edge-1.

5b-chat

Second, to assess the stability of semantic in-
tegration between adjacent levels, we measured

the similarity between high-level summaries and
the concatenated descriptions of their immediate
lower-level tags. The results, presented in Table 11,
show consistently high similarity scores averag-
ing around 0.8 (peaking at 0.8509 for Level 4).
This high degree of semantic consistency between
neighboring levels confirms that the DAG-based
structure ensures stable and effective inheritance of
meaning throughout the tag chain.

Depth

Cosine Sim Avg

1 (root)
2
3
4
5
6
7
8

0.7916
0.8248
0.8478
0.8509
0.8381
0.8341
0.8378
0.7427

Table 11: Cosine similarity for adjacent level inheritance

B.4 Evaluation Metric Consistency Analysis

To validate the coherence of our evaluation frame-
work, we conducted a consistency analysis between
the individual dimension metrics (Comprehensive-
ness, Diversity, and Empowerment) and the holistic
Overall score on the UltraDomain-cs dataset. As
presented in Table 12, all three metrics show high
alignment with the final Overall judgment. Specifi-
cally, Empowerment demonstrates the highest con-
sistency at 96.40%, followed by Comprehensive-
ness (92.53%) and Diversity (84.53%). This strong
correlation indicates that the evaluation model’s
scoring logic is robust and internally logical. Con-
sequently, these results suggest that the Overall
ranking can be effectively determined by aggre-
gating the assessments from these three specific
dimensions, reinforcing the validity of our multi-
faceted evaluation approach.

Consistency Pair

Consistency Ratio

Comprehensiveness and Overall
Diversity and Overall
Empowerment and Overall

92.53%
84.53%
96.40%

Table 12: Consistency analysis between dimension met-
rics and overall score

B.5 LLM-as-a-Judge Consistency Analysis

We further analyze the inter-consistency among
these six evaluators on the UltraDomain-cs dataset.
As shown in Table 13, the results indicate a high
degree of agreement. Specifically, approximately
64.1% of the samples received identical scores
from all six judges (6/6 consistency). When consid-
ering majority voting (agreement from at least 5 out
of 6 judges), the consistency ratio rises to 82.4%,
and it reaches 93.9% when allowing for a wider
margin (at least 4 out of 6). This high level of con-
vergence validates the reliability of our evaluation
outcomes.

Consistency Level

Ratio (%)

6/6 (Full Agreement)
≥5/6 (Strong Majority)
≥4/6 (Simple Majority)

64.1
82.4
93.9

Table 13: Consistency analysis among six evaluators

B.6 Knowledge Graph Construction

Robustness Analysis

To validate the robustness of TagRAG, we construct
a knowledge graph for the same document twice on
the UltraDomain-cs dataset under the Qwen3-4B
default settings (temperature=0.6, top-k=20, top-
p=0.95). The results are presented in Table 14.
In the two knowledge graph constructions, there
were a large number of overlapping object tags
and tag chains. And, some object tags are differ-
ent simply because they are represented separately,
e.g., DATA- AND LEGAL-RELATED QUERIES
are represented separately as DATA-RELATED
QUERIES and LEGAL-RELATED QUERIES. In
terms of entity description and summary, which
TagRAG pays more attention to, the two graph
constructions show a high degree of semantic sim-
ilarity. This demonstrates the consistency and re-
liability of our approach in generating meaningful
knowledge representations.

B.7 Statistics of Knowledge Graph

Construction

We report the scale of knowledge graphs con-
structed by TagRAG and the baselines, as shown in
Table 15. LightRAG extracts the least number of
entities and relationships, resulting in its weakest
knowledge representation. GraphRAG and Mini-
RAG capture huge amounts of entities, but the rela-

Metric

Result

Explanation

Object Tag Jaccard
Object Tag Cosine
Tag Chain Jaccard
Summary Cosine

0.6735
0.9176
0.7396
0.9229

Jaccard similarity of object tags in two knowledge graphs
Semantic similarity of descriptions for the same object tags
Jaccard similarity of tag chains in two knowledge graphs
Semantic similarity of domain tag summaries in two knowledge graphs

Table 14: Knowledge graph construction robustness analysis

tional connections are not as adequate as TagRAG.
This makes the knowledge of the graphs they con-
struct insufficiently connected to produce a global
view.

Agri

CS

Legal Mix

NaiveRAG

Docs
Chunks

12
1756

10
1858

94
4294

61
579

GraphRAG

Entities
Relationships

38059
33781

29803
27598

35817
49163

14393
11114

different domains and adapt to cross-domain appli-
cation scenarios.

B.9 Case Study

To intuitively reflect the effect of TagRAG, we
demonstrate a query case for the UltraDomain CS
corpus in Table 16 - 19. In these cases, we can
see that TagRAG is able to generate global analy-
ses and responses, resulting in a complete lead in
the four metrics of Comprehensiveness, Diversity,
Empowerment, and Overall.

LightRAG

C Prompts

We list the prompts involved in knowledge graph
construction, retrieval enhancement generation,
and experiments, including question generation,
evaluation, object tag keyword extraction, domain
tag chain organization, domain-centric knowledge
fusion and tag knowledge-fused generation.

Entities
Relationships

19153
911

18737
2787

19634
4008

7592
266

MiniRAG

Entities
Relationships

42777
22218

35679
20272

45381
37816

16398
9443

Vo
Eo
Vd
Ed
Eod
Entities
Relationships

TagRAG

16086
29778
2893
4333
11462
18979
45534

14768
21822
1869
2886
7585
16637
32258

18479
43076
2489
4257
11819
20968
59096

7663
7941
2227
3568
3967
9890
15421

Table 15: Statistics of knowledge graph construction

B.8 Cross-domain Visual Analysis

Leveraging the mapping of domain tag chains,
TagRAG enables support for cross-domain sce-
narios. As illustrated in Figure 6, the predefined
root domain tag “ALL DISCIPLINES” serves as
the anchor for the entire domain knowledge graph,
with diverse domains (e.g., social sciences, histori-
cal studies) interconnected in a hierarchical struc-
ture to guide cross-domain object tags. For in-
stance, the object tag “THIRTY YEARS’ WAR” links
to the root domain via the chain “HISTORICAL
STUDIES - EUROPEAN HISTORY”, while another
object tag “BERT” maps to “NATURAL LANGUAGE
PROCESSING”, which comes from a completely dif-
ferent field. This demonstrates that TagRAG pos-
sesses the capability to integrate knowledge across

Figure 6: Demonstration of tag chains on UltraDomain Mix.

Query
TagRAG

How can we select the most important features for the model using feature selection techniques?
Selecting the most important features for a machine learning model is a critical step in the data preprocessing
pipeline. It helps improve model performance, reduce overfitting, and enhance interpretability. Feature
selection techniques can be broadly categorized into three types: filter methods, wrapper methods, and
embedded methods. Each approach has its own advantages and is suitable for different scenarios depending
on the problem, data, and model type.
Filter Methods
Filter methods are the simplest and most computationally efficient techniques. They evaluate the relevance of
features based on statistical measures and do not consider the model structure. These methods are ...
Wrapper Methods
Wrapper methods evaluate the importance of features by training and testing different subsets of features.
These methods are more computationally intensive than filter methods but can lead to better ...
Embedded Methods
Embedded methods incorporate feature selection during the model training process. These methods are
model-specific and are often used in regularization-based models. ...
Practical Considerations
1. Domain Knowledge: ... 2. Data Quality: ... 3. Computational Resources: ... 4. Model Type: ...
In summary, feature selection is a crucial step in the machine learning pipeline that helps in building more
efficient, accurate, and interpretable models. The choice of method depends on the specific problem, data
characteristics, and computational resources available. By carefully selecting the most important features, we
can significantly improve the performance of our models.

Evaluation

NaiveRAG Feature selection is a crucial step in building effective machine learning models, as it helps to identify the
most relevant variables that contribute to the model’s predictive performance while reducing complexity and
improving interpretability. The document outlines several feature selection techniques and their importance in
the context of model training and evaluation.
One of the key approaches mentioned is backward selection, which involves starting with all features and
iteratively removing the least important ones until a stopping criterion is met. This method is particularly
useful for reducing the number of features while maintaining model performance. ...
In addition to backward selection, the document discusses the use of multi-objective optimization strategies,
which aim to balance the trade-off between model performance and feature reduction. ...
The document also provides an example of feature selection in the context of the wine quality dataset, where
the goal is to predict wine quality based on ...
In summary, feature selection techniques such as backward selection, multi-objective optimization, and the
use of advanced optimization algorithms are essential for identifying the most important features for a model.
These techniques not only improve model performance but also enhance the interpretability and efficiency of
the model.
“Comprehensiveness”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 provides a detailed
and well-rounded overview of various feature selection techniques, covering filter methods, wrapper methods,
and embedded methods. It includes specific examples such as Pearson’s correlation coefficient, mutual
information, RFE, and Lasso regression, among others. In contrast, Answer 2 focuses primarily on backward
selection and multi-objective optimization, providing less overall coverage of the different types of feature
selection methods.” },
“Diversity”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 presents a variety of techniques
across different categories (filter, wrapper, and embedded), with examples from both statistical and machine
learning methods. It also includes practical considerations like domain knowledge and computational resources.
Answer 2 is more narrowly focused on backward selection and multi-objective optimization, offering fewer
perspectives on feature selection.” },
“Empowerment”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 gives readers a deeper un-
derstanding of the trade-offs and applications of different feature selection methods, such as the computational
resources required and the types of models they suit best. It also includes practical tips, such as the importance
of domain knowledge. This enables the reader to make more informed decisions about which technique to use.
Answer 2, while informative, focuses more on specific methods without fully empowering the reader to make
broad judgments about feature selection.” },
“Overall Winner”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Although Answer 2 is more direct,
Answer 1 is the overall winner because it provides a more comprehensive, diverse, and empowering explanation.
It covers a wider range of feature selection techniques and practical considerations, helping readers gain a
thorough understanding of how to approach feature selection in different contexts. This broader perspective
makes Answer 1 a more valuable resource for decision-making in feature selection.” }

Table 16: Case study: evaluation of TagTAG v.s. NaiveRAG with Qwen3-4B

Query
TagRAG

How can we select the most important features for the model using feature selection techniques?
Selecting the most important features for a machine learning model is a critical step in the data preprocessing
pipeline. It helps improve model performance, reduce overfitting, and enhance interpretability. Feature
selection techniques can be broadly categorized into three types: filter methods, wrapper methods, and
embedded methods. Each approach has its own advantages and is suitable for different scenarios depending
on the problem, data, and model type.
Filter Methods
Filter methods are the simplest and most computationally efficient techniques. They evaluate the relevance of
features based on statistical measures and do not consider the model structure. These methods are ...
Wrapper Methods
Wrapper methods evaluate the importance of features by training and testing different subsets of features.
These methods are more computationally intensive than filter methods but can lead to better ...
Embedded Methods
Embedded methods incorporate feature selection during the model training process. These methods are
model-specific and are often used in regularization-based models. ...
Practical Considerations
1. Domain Knowledge: ... 2. Data Quality: ... 3. Computational Resources: ... 4. Model Type: ...
In summary, feature selection is a crucial step in the machine learning pipeline that helps in building more
efficient, accurate, and interpretable models. The choice of method depends on the specific problem, data
characteristics, and computational resources available. By carefully selecting the most important features, we
can significantly improve the performance of our models.

GraphRAG Feature selection techniques are essential for identifying the most important features for a model, as they help
reduce dimensionality, improve model performance, and enhance interpretability. These techniques can be
broadly categorized into three main types: filter methods, wrapper methods, and embedded methods. Filter
methods evaluate features based on ... . Wrapper methods, on the other hand, use iterative model training to
select ... . Embedded methods integrate feature selection directly into ... .
The choice of technique depends on the specific problem, the type of data, and the goals of the modeling task.
For instance, filter methods are computationally efficient and suitable for high-dimensional datasets, while
wrapper methods may provide better performance but are more computationally intensive. Embedded methods
are particularly useful when the model inherently performs feature selection, such as in regularization-based
algorithms. Additionally, techniques like ... .
The importance of feature selection lies in its ability to enhance model interpretability, reduce overfitting,
and improve computational efficiency. By focusing on the most relevant features, models can achieve better
accuracy and generalization, making them more effective for real-world applications. However, it is crucial to
evaluate the impact of feature selection on model performance through validation techniques to ensure that
the selected features contribute meaningfully to the model’s predictive power. Ultimately, the most effective
feature selection approach will depend on the specific characteristics of the dataset and the objectives of the
modeling task.
“Comprehensiveness”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 offers a highly
detailed breakdown of the three main feature selection techniques—filter, wrapper, and embedded meth-
ods—with specific sub-methods under each category (e.g., Pearson correlation, RFE, Lasso). It also includes
practical considerations such as domain knowledge, data quality, and model type, which extend the depth of
coverage beyond just naming methods. Answer 2, while accurate, is more concise and general.”},
“Diversity”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 presents a richer variety of
perspectives and techniques, covering a broader spectrum of tools within each method type and touching on
ensemble models like Random Forest, as well as XGBoost and LightGBM. It also discusses non-technical
factors (e.g., domain knowledge, computational resources), whereas Answer 2 is more method-focused and
omits these complementary angles.”},
“Empowerment”: { “Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 is more empowering as
it equips the reader with both theoretical knowledge and practical guidance. It explains when and why to
use each method, provides context on computational cost, and suggests model-specific strategies. Answer 2
emphasizes general insights but lacks actionable detail for applying the techniques effectively.”},
“Overall Winner”: { “Winner”: “Answer 1 (TagRAG)’, “Explanation”: “Answer 1 is the overall winner
due to its superior comprehensiveness, greater diversity of content, and better empowerment of the reader.
While Answer 2 is more direct, the depth and breadth of Answer 1 make it more valuable for users looking to
understand and apply feature selection techniques effectively”}

Evaluation

Table 17: Case study: evaluation of TagTAG v.s. GraphRAG with Qwen3-4B

Query
TagRAG

How can we select the most important features for the model using feature selection techniques?
Selecting the most important features for a machine learning model is a critical step in the data preprocessing
pipeline. It helps improve model performance, reduce overfitting, and enhance interpretability. Feature
selection techniques can be broadly categorized into three types: filter methods, wrapper methods, and
embedded methods. Each approach has its own advantages and is suitable for different scenarios depending
on the problem, data, and model type.
Filter Methods
Filter methods are the simplest and most computationally efficient techniques. They evaluate the relevance of
features based on statistical measures and do not consider the model structure. These methods are ...
Wrapper Methods
Wrapper methods evaluate the importance of features by training and testing different subsets of features.
These methods are more computationally intensive than filter methods but can lead to better ...
Embedded Methods
Embedded methods incorporate feature selection during the model training process. These methods are
model-specific and are often used in regularization-based models. ...
Practical Considerations
1. Domain Knowledge: ... 2. Data Quality: ... 3. Computational Resources: ... 4. Model Type: ...
In summary, feature selection is a crucial step in the machine learning pipeline that helps in building more
efficient, accurate, and interpretable models. The choice of method depends on the specific problem, data
characteristics, and computational resources available. By carefully selecting the most important features, we
can significantly improve the performance of our models.

LightRAG To select the most important features for a model using feature selection techniques, you can follow these steps

Evaluation

based on the information provided in the Knowledge Base:
1. Understand the Purpose of Feature Selection: Feature selection is the process of selecting ... .
2. Use Feature Selection Techniques: There are several feature selection techniques that can ... .
3. Apply Feature Selection Algorithms: The Knowledge Base mentions that feature selection can ... .
4. Evaluate Feature Importance: After selecting the features, it is important to evaluate ... .
5. Integrate Feature Selection with Model Training: Once the relevant features are selected, they ... .
6. Validate the Selected Features: Finally, the selected features should be validated using ... .
By following these steps, you can effectively select the most important features for your model using feature
selection techniques, leading to improved model performance and interpretability.
“Comprehensiveness”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 provides a highly
detailed breakdown of the different feature selection methods (filter, wrapper, and embedded), including
specific techniques and algorithms within each category. It offers a thorough explanation of statistical measures,
domain knowledge considerations, and computational resources, making it more comprehensive in covering all
the necessary aspects of feature selection. In contrast, Answer 2 is relatively high-level and misses some of the
specific techniques and broader considerations like the different types of feature selection methods.”},
“Diversity”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 offers a wide range of techniques
and insights into feature selection methods, discussing multiple algorithms within each category (e.g., Pearson’s
correlation, Recursive Feature Elimination, Lasso, Random Forest) and highlighting their respective strengths
and applications. It also touches on practical aspects like domain knowledge and computational resources. On
the other hand, Answer 2 presents fewer perspectives and sticks more closely to general steps, without delving
into diverse methodologies or offering a variety of relevant examples.”},
“Empowerment”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 empowers the reader by
explaining the different techniques in detail and providing concrete examples (e.g., Pearson’s correlation, RFE,
Lasso, and Random Forest). It helps the reader understand how to apply each method and why one might
choose one over another based on data, model type, and resources. It provides enough depth to make informed
judgments. Answer 2, while giving a process-oriented approach, doesn’t provide enough detail on how to
evaluate or apply these methods in practice, which reduces the reader’s ability to fully grasp how to make
decisions about feature selection.”},
“Overall Winner”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 is the overall winner due to
its comprehensive coverage, diversity of insights, and empowerment of the reader with clear examples and
practical considerations. It offers a far more detailed and multifaceted view of feature selection techniques,
enabling the reader to make informed decisions about which approach to use in various scenarios. While Answer
2 is more direct and streamlined, it lacks the depth and richness necessary to provide a full understanding of
the topic.”}

Table 18: Case study: evaluation of TagTAG v.s. LightRAG with Qwen3-4B

Query
TagRAG

MiniRAG

Evaluation

How can we select the most important features for the model using feature selection techniques?
Selecting the most important features for a machine learning model is a critical step in the data preprocessing
pipeline. It helps improve model performance, reduce overfitting, and enhance interpretability. Feature
selection techniques can be broadly categorized into three types: filter methods, wrapper methods, and
embedded methods. Each approach has its own advantages and is suitable for different scenarios depending
on the problem, data, and model type.
Filter Methods
Filter methods are the simplest and most computationally efficient techniques. They evaluate the relevance of
features based on statistical measures and do not consider the model structure. These methods are ...
Wrapper Methods
Wrapper methods evaluate the importance of features by training and testing different subsets of features.
These methods are more computationally intensive than filter methods but can lead to better ...
Embedded Methods
Embedded methods incorporate feature selection during the model training process. These methods are
model-specific and are often used in regularization-based models. ...
Practical Considerations
1. Domain Knowledge: ... 2. Data Quality: ... 3. Computational Resources: ... 4. Model Type: ...
In summary, feature selection is a crucial step in the machine learning pipeline that helps in building more
efficient, accurate, and interpretable models. The choice of method depends on the specific problem, data
characteristics, and computational resources available. By carefully selecting the most important features, we
can significantly improve the performance of our models.
Selecting the most important features for a model is a crucial step in the machine learning pipeline, as it can
significantly impact the model’s performance, interpretability, and efficiency. Feature selection techniques help
... . Here’s how you can approach feature selection using various techniques:
1. Understanding the Problem and Data Before applying any feature selection techniques, it’s ... .
2. Feature Selection Techniques There are several feature selection techniques, which can ... .
3. Feature Selection in Practice To apply feature selection in practice, you can follow these steps: ... .
4. Example: Using Lasso Regression for Feature Selection Here’s an example of using Lasso Regression for
feature selection in Python using ... .
5. Conclusion Feature selection is a critical step in the machine learning pipeline. By selecting the most
important features, you can improve the model’s performance, reduce overfitting, and make the model more
interpretable. The choice of feature selection technique depends on the specific problem, the size of the dataset,
and the computational resources available.
“Comprehensiveness”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 is more comprehensive
as it goes into greater detail about each feature selection technique, explaining the methods in-depth, including
the differences between various types of techniques (filter, wrapper, and embedded methods). It also discusses
practical considerations and highlights the importance of domain knowledge, data quality, and model type,
which adds value and depth to the response.”},
“Diversity”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 presents a wider variety of feature
selection techniques, offering diverse methods within each category (filter, wrapper, and embedded). It also
discusses additional considerations like computational resources, model type, and domain knowledge, giving a
broader range of insights on the topic.”},
“Empowerment”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Answer 1 empowers the reader by
thoroughly explaining each technique’s use, advantages, and practical scenarios. It also provides valuable
insights on how the selection method should align with the problem at hand, giving readers the tools to make
informed decisions based on their specific context.”},
“Overall Winner”: {“Winner”: “Answer 1 (TagRAG)”, “Explanation”: “Although Answer 2 is more direct,
Answer 1 provides a more comprehensive, diverse, and empowering response that thoroughly covers the topic,
making it the overall winner. It offers in-depth explanations, a variety of methods, and detailed guidance, which
would better equip the reader to understand and apply feature selection techniques in different scenarios.”}

Table 19: Case study: evaluation of TagTAG v.s. MiniRAG with Qwen3-4B

Prompt of question generation

Given the following description of a dataset: {total_description}. Please identify 5 potential users who would engage
with this dataset. For each user, list 5 tasks they would perform with this dataset. Then, for each (user, task) combination,
generate 5 questions that require a high-level understanding of the entire dataset. Output the results in the following
structure:
- User 1: [user description]

- Task 1: [task description]

- Question 1:
...
- Question 5:

...
- Task 5: [task description]

...
- User 5: [user description]

...

Prompt of evaluation

—Role—
You are an expert tasked with evaluating two answers to the same question based on three criteria: **Comprehensive-
ness**, **Diversity**, **Empowerment**, and **Directness**.
You will evaluate two answers to the same question based on three criteria: **Comprehensiveness**, **Diversity**,
and **Empowerment**.
- **Comprehensiveness**: How much detail does the answer provide to cover all aspects and details of the question?
- **Diversity**: How varied and rich is the answer in providing different perspectives and insights on the question?
- **Empowerment**: How well does the answer help the reader understand and make informed judgments about the
topic?
For each criterion, choose the better answer (either Answer 1 or Answer 2) and explain why. Then, select an overall
winner based on these three categories.
Here is the question: {query}
Here are the two answers:
**Answer 1:** {answer1}
**Answer 2:** {answer2}

Evaluate both answers using the three criteria listed above and provide detailed explanations for each criterion. Output
your evaluation in the following JSON format:
{“Comprehensiveness”: {“Winner”: “[Answer 1 or Answer 2]”, “Explanation”: “[Provide explanation here]”},

“Diversity”: {“Winner”: “[Answer 1 or Answer 2]”, “Explanation”: “[Provide explanation here]”},
“Empowerment”: {“Winner”: “[Answer 1 or Answer 2]”, “Explanation”: “[Provide explanation here]”},
“Overall Winner”: {“Winner”: “[Answer 1 or Answer 2]”, “Explanation”: “[Summarize why this answer is the overall

winner based on the three criteria]”}}

Prompt of object tag keyword extraction

—Goal—
Given a domain-specific text document and a list of keyword types, summarize keywords from the text and generate
their relationships. Use {language} as output language.
—Steps—
1. Summarize keywords from the text. For each summarized keyword, generate the following information:
- keyword_name: Name of the keyword, use same language as input text. If English, capitalized the name.
- keyword_type: Type of the keyword that can classify the keyword.
- keyword_description: Comprehensive description of the keyword’s attributes and activities
Format each keyword as (“keyword”{tuple_delimiter}< keyword_name >{tuple_delimiter}< keyword_type >
{tuple_delimiter}< keyword_description >)
2. From the keywords summarized in step 1, generate all pairs of (source_keyword, target_keyword) that are *clearly
related* to each other.
Don’t create source_keyword or target_keyword that are not summarized in step 1.
For each pair of related keywords, generate the following information:
- source_keyword: name of the source keyword, as summarized in step 1
- target_keyword: name of the target keyword, as summarized in step 1
- relationship_description: explanation as to why you think the source keyword and the target keyword are related to
each other
Format each relationship as (“relationship”{tuple_delimiter}< source_keyword >{tuple_delimiter}
< target_keyword >{tuple_delimiter}< relationship_description >)
3. Return output in {language} as a single list of all the keywords and relationships generated in steps 1 and 2. Use
**{record_delimiter}** as the list delimiter.
4. When finished, output {completion_delimiter}

—Examples—
{examples}
—Real Data—
Text: {input_text}
Output:

Prompt of domain tag chain organization

—Goal—
Given a domain tag with its description and an object tag with its description, generate the relationship chain between
them.
Use {language} as output language.
—Steps—
1. Generate the relationship chain between the domain tag and the object tag. Present all domain tags consisting of the
following information:
- domain_name: Name of the domain, use same language as input text. If English, capitalized the name.
- domain_description: Comprehensive description of the domain tag.
Format each domain tag as < domain_name >{explanation_delimiter}< domain_description > and connect
domain tags with **{inference_delimiter}**.
2. Generate the relationship description between the object tag and the generated relationship chain in step 1. Use
**{tuple_delimiter}** as the delimiter.
3. Return output in {language} as a single relationship chain generated in step 1 and a relationship description generated
in step 2.
4. When finished, output {completion_delimiter}
—Examples—
{examples}
—Real Data—
Domain tag name: {domain_tag_name}
Domain tag description: {domain_tag_description}
Object tag name: {object_tag_name}
Object tag description: {object_tag_description}
Output:

Prompt of domain-centric knowledge fusion

—Goal—
Given a chain of domain tags with their descriptions, the summary of the chain, relevant object tags with their
descriptions and the relationship descriptions, summarize the domain by injecting these object tags at a high level. Use
{language} as output language.
—Domain tag chain—
{domain_tag_chain}
—Chain summary—
{chain_summary}
—Object tags—
{object_tags}
—relationships—
{relationships}
Output:

Prompt of tag knowledge-fused generation

—Role—
You are a helpful assistant responding to questions about data in the tables provided.

—Goal—
Generate a response of the target length and format that responds to the user’s question, summarizing all information in
the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
Do not include information where the supporting evidence for it is not provided.

—Target response length and format—
{response_type}
—Data tables—
{context_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.

