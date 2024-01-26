---
layout: page
title: Schedule
permalink: /neurips2023/schedule
---
<style>
/* div {
    text-align: center;
    margin: 0 auto;
} */
</style>


👉 [WANT poll](https://forms.gle/cJHmvtZvdbMuHzxh9) - Tell us your insights and thought about efficient training of neural networks! Your vote does matter! 

📜 [WANT page at OpenReview](https://openreview.net/group?id=NeurIPS.cc/2023/Workshop/WANT) - Accepted papers (Orals & Posters) are here!

📅 [WANT page at Whova](https://whova.com/portal/webapp/cnips_202312/Agenda/3512322) - Add to your NeurIPS agenda!

Workshop on Advancing Neural Network Training (WANT) will take place on **December 16, 2023**
- **offline**: at the venue of the [NeurIPS 2023 conference](https://neurips.cc) in New Orleans, USA, **room 243-245**,
- **online**: with [streaming from the venue](https://neurips.cc/virtual/2023/workshop/66493) 🎥, poster session and networking in Gather Town 🏰.

<!-- 
<table><tbody>
<tr>
  <th> Time (New Orleans) </th>
  <th> 
  
  **Morning** 
  
  </th>
<tr>
<tr>
  <td>
  08:15 - 08:45 
  </td>
  <td>
<details>
<summary> 

Invited talk <br> **Rematerialization algorithms for Memory-efficient learning** <br> *Lionel Eyraud-Dubois* 

</summary> 

**Abstract:** The training phase of Deep Neural Networks is often a very memory-intensive procedure, where large amounts of intermediate data have to be kept in memory during one iteration. One possible approach to reduce memory usage is rematerialization, aka gradient checkpointing, where some intermediate data are recomputed when needed rather than kept in memory. This provides a tradeoff between memory usage and recomputation time. In this talk I will present several approaches for the optimization problem, where one wants to minimize the recomputation time given a fixed memory budget. The corresponding algorithms have been implemented in easy-to-use libraries for the PyTorch framework, which can significantly reduce memory usage with reasonable overhead.
</details> 
  </td>
<tbody></table>
 -->



| Time (New Orleans) | **Morning**   | 
|:-----------------------------------------------------------------:|
| 08:15 - 08:50 | Poster placement                             | 
| 08:50 - 09:00 | Welcome speech from Organizers 🎥  &emsp; [slides](https://drive.google.com/file/d/1bBQZKTt6N958XLmj2TflXy_pWBYT8qCf/view?usp=share_link) <br> *Julia Gusak*                               | 
| 09:00 - 09:30 | Invited talk 🎥  &emsp; [slides](https://drive.google.com/file/d/1rzuM03lbg2y4TfK80P4gzOfCvTXB7N5C/view?usp=share_link) <br> **A data-centric view on workflows that couple HPC with large-scale models** <br> *Ana Gainaru* <details> In recent years, scientific computing workloads at HPC facilities have been undergoing a significant shift. While traditionally dominated by numerical simulations, these facilities are increasingly handling AI/ML applications for training and inference, processing and producing ever-increasing amounts of scientific data. Despite the focus on optimizing the execution of new AI/HPC workflows, little attention has been paid to the I/O runtime challenges they present. This talk aims to address that gap by analyzing these emerging trends from an I/O perspective. We will explore the performance of the multilayer high-performance I/O systems under the strain of these new workflows that combine traditional HPC techniques with AI interacting in new challenging ways.</details>                       | 
| 09:30 - 10:00 | Invited talk 🎥  &emsp; [slides](https://drive.google.com/file/d/1iGLFqO-Rd3wBUUqf1pp8KgA5aCCmeWsO/view?usp=share_link) <br> **Rematerialization algorithms for Memory-efficient learning** <br> *Lionel Eyraud-Dubois* <details> The training phase of Deep Neural Networks is often a very memory-intensive procedure, where large amounts of intermediate data have to be kept in memory during one iteration. One possible approach to reduce memory usage is rematerialization, aka gradient checkpointing, where some intermediate data are recomputed when needed rather than kept in memory. This provides a tradeoff between memory usage and recomputation time. In this talk I will present several approaches for the optimization problem, where one wants to minimize the recomputation time given a fixed memory budget. The corresponding algorithms have been implemented in easy-to-use libraries for the PyTorch framework, which can significantly reduce memory usage with reasonable overhead </details>                    | 
| 10:00 - 10:30 | Coffee break  🏰                                | 
| 10:30 - 11:00| Invited talk 🎥 &emsp; [slides](https://drive.google.com/file/d/1DWvfChg7kAYuG5T-wleAeHhXT4Isrh8N/view?usp=share_link) <br> **Navigating the Landscape of Enormous AI Model Training** <br> *Yang You* <details> The proliferation of large models based on Transformers has outpaced advances in hardware, resulting in an urgent need for the ability to distribute enormous models across multiple GPUs. Despite this increasing need, the absence of established best practices for selecting an optimal strategy persists, owing to the extensive expertise required in High-Performance Computing (HPC), Deep Learning (DL), and distributed systems. These challenges have motivated both AI and HPC developers to delve into pivotal questions: How can the training and inference efficiency of large models be enhanced to minimize costs? How can larger AI models be accommodated, even with limited resources? What measures can be taken to facilitate broader community access to large models and large-scale applications? In this talk, I will discuss potential solutions to these challenges by exploring hybrid parallelisms, heterogeneous memory management, and the design of user-friendly frameworks such as our open-source systemic solution: Colossal-AI (https://github.com/hpcaitech/ColossalAI). </details>                       | 
| 11:00 - 11:30 | Invited talk 🎥 &emsp; [slides](https://drive.google.com/file/d/1IN_X2ldi3M5R_kdLbBzpNrX3pTBUtkiN/view?usp=share_link) <br> **Enabling efficient trillion parameter scale training for deep learning models** <br> *Tunji Ruwase* <details> Deep Learning (DL) is driving unprecedented progress in a wide range of Artificial Intelligence domains, including natural language processing, vision, speech, and multimodal. However, sustaining this AI revolution requires practical solutions to the extreme demands of model scaling on the compute, memory, communication and storage components of modern computing hardware. To address this challenge, we created a deep learning optimization library called DeepSpeed to make distributed model training and inference efficient, effective, and easy on commodity hardware. This talk will focus on DeepSpeed training optimizations, particularly on ZeRO and DeepSpeed-MoE, which help to address the memory and compute requirements of extreme model scaling. </details>                         | 
| 11:30 - 12:00 | Contributed talks 🎥 | 
| 11:31 - 11:36 | Contributed talk 🎥 <br> **Training and inference of large language models using 8-bit floating point** <br> *Sergio Perez, Yan Zhang, James Briggs, Charles Blake, Josh Levy-Kramer, Paul Balanca, Carlo Luschi, Stephen Barlow, Andrew Fitzgibbon*   |
| 11:37 - 11:42 | Contributed talk 🎥 <br> **MatFormer: Nested Transformer for Elastic Inference** <br> *Fnu Devvrit, Sneha Kudugunta, Aditya Kusupati, Tim Dettmers, Kaifeng Chen, Inderjit Dhillon, Yulia Tsvetkov, Hannaneh Hajishirzi, Sham Kakade, Ali Farhadi, Prateek Jain*    |
| 11:43 - 11:48 | Contributed talk 🎥 <br>  **Sparse Backpropagation for MoE Training** <br> *Liyuan Liu, Jianfeng Gao · Weizhu Chen*  |
| 11:49 - 11:54 | Contributed talk 🎥 <br> **Efficient Parallelization Layouts for Large-Scale Distributed Model Training** <br> *Johannes Hagemann, Samuel Weinbach, Konstantin Dobler, Maximilian Schall, Gerard de Melo*   |
| 11:55 - 12:00 | Contributed talk 🎥 <br> **CoTFormer: More Tokens With Attention Make Up For Less Depth** <br> *Amirkeivan Mohtashami, Matteo Pagliardini, Martin Jaggi*  |


| Time (New Orleans) | **Afternoon**    |
|:-----------------------------------------------------------------:|
| 12:00 - 13:00 | Lunch  🏰 | 
| 13:00 - 13:30 | Lunch (offline) \| Poster session (Gather Town) 🏰 
| 13:30 - 14:00 | Poster session (offline + Gather Town) 🏰                                | 
| 14:00 - 14:30 | Invited Talk 🎥 &emsp; [slides](https://drive.google.com/file/d/1cK6o_2KM_7IJ0EQ1hTy6tkO-5C36mWVU/view?usp=share_link) <br> **Crafting Computational Efficiency for Large Models: Training Recipes, Scaling Strategies and Sparsity Sorcery with Specialized Hardware** <br> *Natalia Vassilieva* <details>  Large models are shifting “what’s possible” with AI. Brute-force scaling of model parameter count increases model capacity, and when presented with enough training data, has shown remarkable results. However, the advantages of large-scale models come at a price of steep increase in system complexity and infrastructure cost. Training and serving these models is an engineering challenge and is very expensive. Even minor errors in model design or training procedure can result in significant waste of resources. At Cerebras we have trained our share of large language models and learned along the way how to train these models efficiently to get “the biggest bang for the buck”. In this talk we will share our experience and insights from training various LLMs. In addition to techniques for compute efficient training of dense models, we will look into benefits of sparse training and inference on Cerebras hardware, designed to take full advantage of all types of sparsity. </details>                         | 
| 14:30 - 15:00 | Invited Talk 🎥 <br> **The MosaicML Approach to LLM Training** <br> *Johnathan Frankle, Naveen Rao* <details> In this talk, I will describe the many tools and approaches that MosaicML uses to train its LLMs. We rely heavily on and contribute to a variety of open-source frameworks that form the backbone of our product. Since our business is to make it possible for anyone to train their own LLM from scratch, our stack must be robust to many different data distributions and use-cases, and it must be simple, straightforward, and extensible enough for a wide variety of end users to work with. This presents unique demands and constraints that have shaped the way we build our toolchain. </details>                        | 
| 15:00 - 15:30 | Coffee break 🏰                                | 
| 15:30 - 16:00 | Invited Talk 🎥 <br> **Efficient LLM Training and Inference on GPUs** <br> *Mohammad Shoeybi, Bryan Catanzaro* <details> Training and inference of large transformer models is one of the most important computational challenges of modern AI. Systems for training these models must be highly scalable and run at extreme efficiency, because the amount of work necessary to converge a model can be extraordinarily large. Inference needs to be fast and accommodate different query sizes. In this talk, I'll discuss the work we have been doing at NVIDIA to optimize systems for Large Language Model training and inference on GPUs. I will present different parallelism techniques we are using in our LLM framework Megatron-LM and will discuss how parallelism techniques can be combined to maximize the training throughput of large models while retaining strict optimizer semantics. I will discuss optimizations techniques for inference and methods to accelerate inference and reduce memory fragmentation. </details>                       | 
| 16:00 - 16:50 | Panel Discussion 🎥 &emsp; [slides](https://drive.google.com/file/d/1NfKuSifNZbHcpip1qx7Imo5ryPkcei8o/view?usp=share_link) <br>  *Ana Gainaru, Lionel Eyraud-Dubois, Tunji Ruwase, Natalia Vassilieva, Mohammad Shoeybi, Jean Kossaifi* |
| 16:50 - 17:00 | Closing remarks 🎥 |
| 17:00 - 17:30 | Poster session (offline + Gather Town) 🏰                                | 

<!-- | 16:00 - 16:50 | Panel Discussion <br> {::nomarkdown}<ul><li>Yang You </li> <li> Olatunji Ruwase </li>  <li> Natalia Vassilieva </li>  <li>Mohammad Shoeybi </li> <li>Jean Kossaifi</li></ul>{:/} | -->

<!-- | **Activity (morning)**    | **Duration** |
|-----------------------------------------------------------------|--------------|---------------------------------------------------------------|--------------|
| Welcome speech from organizers                                  | 10 mins      | 
| Invited Talks (3-4)                               | 15+5 mins (each)   | 
| Coffee break + Poster Session                                   | 30 mins      |
| Panel Discussion with invited speakers  | 40 mins      |
| Lightning session            | 40   mins    | 


| **Activity (afternoon)**    | **Duration** |
|-----------------------------------------------------------------|--------------|---------------------------------------------------------------|--------------|
| Lunch break + Poster Session                                  | 90 mins      |
| Contributed talk (Best Paper)                                 | 10 mins      |
| Invited talks (3-4)                            | 15+5 mins  (each)   |
| Coffee break + Poster Session                                 | 30 mins      |
| Panel Discussion with invited speakers  | 40 mins      | -->