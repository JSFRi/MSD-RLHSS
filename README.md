# MSD-RLHSS: Management of Scientific Datasets in Reinforcement Learning based Hierarchical Storage System

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

![github](https://user-images.githubusercontent.com/37439749/216436763-e8b2e9c6-81d5-4453-b3ee-7e310ea9b974.png)

## Table of Contents

+ [About](#about)
    + [Code Locations](#codeloc)
    + [Poster & Extended Abstract](#docloc)
    + [Information About The Dataset](#datasetinfo)
+ [Getting Started](#getting_started)
    + [Prerequisites](#prerequisites)
+ [Setting Up](#installing)
+ [Running the code](#run_locally)
    + [Configuration](#configuration)
    + [Running Jupyter](#jupyter)
+ [Acknowledgments](#acknowledgments)

This repository contains the codes for deploying the three-tier HSS (Hierarchical Storage System), implementing 6 migration policies, and running experiments on 4 scientific datasets that we introduced in our paper.

Folder Cloud_dep/ includes the steps to start three instances based on the openstack platform of SNIC Science Cloud (SSC). The three instances are assigned with different sizes and I/O speeds, to act as the three tiers in the HSS.

Policies/ is the folder of all codes of implementing 6 migration policies: RL-based policy, Random Placement, Least Recently Used replacement (LRU), Least Frequently Used replacement (LFU), Maximal/minimal feature policy, and K-means policy. Implementation of each policy is under the folder with the same name of the policy.

Datasets/ contains brief summary of the 4 scientific datasets.

## Acknowledements

This research is supported by the Swedish Foundation for Strategic Research (SSF), project HASTE, under Grant No. 𝐵𝐷15 − 0008. We would also like to acknowledge Swedish National Infrastructure for Computing (SNIC) for providing cloud resources, project number 𝑆𝑁𝐼𝐶 2022/22 − 835 , and support from eSSENCE, a Swedish strategic collaborative research program in e-science.
