# MSD-RLHSS: Data Management of Scientific Applications in a Reinforcement Learning-Based Hierarchical Storage System

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

![github](https://user-images.githubusercontent.com/37439749/216436763-e8b2e9c6-81d5-4453-b3ee-7e310ea9b974.png)

## Table of Contents

+ [About](#about)
+ [Code Locations](#codeloc)
+ [Datasets](#Datasets)
+ [Cloud deployment](#clouddep)
+ [Acknowledgments](#acknowledgments)

## About

This repository contains the codes for deploying the three-tier HSS (Hierarchical Storage System), implementing 6 migration policies, running experiments on the 4 scientific datasets, and generating the results that we introduced in our paper.

## Code Locations <a name = "codeloc"></a>

Folder [Cloud_dep/](Cloud_dep) includes the steps to start three instances based on the openstack platform of SNIC Science Cloud (SSC). The three instances are assigned with different sizes and I/O speeds, to act as the three tiers in the HSS.

[Policies/](Policies) is the folder of all codes of implementing 6 migration policies: RL-based policy, Random Placement, Least Recently Used replacement (LRU), Least Frequently Used replacement (LFU), Maximal/minimal feature policy, and K-means policy. Implementation of each policy is under the folder with the same name of the policy.

[Datasets/](Datasets) contains brief summary of the 4 scientific datasets.

[Results/](Results) includes the results of experiments upon the 4 datasets, in the form of Jupyter notebook. Each notebook contains some breif information about the corresponding dataset, and the results in terms of system response time and etc.

## Datasets

See [Datasets/](Datasets) for more details

## Cloud deployment <a name = "clouddep"></a>

To start the 3-tier HSS on openstack platform, run [start_instances_3tier.py](Cloud_dep/start_instances_3tier.py). If one want to set up different configurations, modify the -cfg.txt files.

## Acknowledgments

This research is supported by the Swedish Foundation for Strategic Research (SSF), project HASTE, under Grant No. 𝐵𝐷15 − 0008. We would also like to acknowledge Swedish National Infrastructure for Computing (SNIC) for providing cloud resources, project number 𝑆𝑁𝐼𝐶 2022/22 − 835 , and support from eSSENCE, a Swedish strategic collaborative research program in e-science.
