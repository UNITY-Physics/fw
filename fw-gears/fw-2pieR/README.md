# 2pieR (Head Circumference)
This gear calculates head circumference from a T2w image. It is based on the

**UNDER DEVELOPMENT**

## Overview

[Usage](#usage)

[FAQ](#faq)

### Summary


### Cite

**license:**
MIT License  

**url:** <>

**cite:**  
Doug Dean III

### Classification

*Category:* analysis

*Gear Level:*

* [ ] Project
* [ ] Subject
* [ ] Session
* [ ] Acquisition
* [x] Analysis

----

### Inputs

* api-key
  * **Name**: api-key
  * **Type**: object
  * **Optional**: true
  * **Classification**: api-key
  * **Description**: Flywheel API key.

### Config

* input
  * **Base**: file
  * **Description**: input file 
  * **Optional**: false


#### Metadata

No metadata currently created by this gear

### Pre-requisites


#### Prerequisite Gear Runs

1. ***dcm2niix***
    * Level: Any
2. ***file-metadata-importer***
    * Level: Any
3. ***file-classifier***
    * Level: Any

#### Prerequisite

## Usage

This section provides a more detailed description of the gear, including not just WHAT
it does, but HOW it works in flywheel

### Description



#### File Specifications

This section contains specifications on any input files that the gear may need

### Workflow

A picture and description of the workflow

```mermaid
  graph LR;
    A[T2w]:::input --> FW;
    FW[FW] --> D2N;
    D2N((dcm2niix)):::gear --> CISO;
    CISO((recon)):::gear --> N4;
    N4((biasCorr)):::gear --> BET;
    BET((HD-BET)):::gear --> VBM;
    VBM[Morphometry]:::container;
    
    classDef container fill:#57d,color:#fff
    classDef input fill:#7a9,color:#fff
    classDef gear fill:#659,color:#fff
```

Description of workflow

1. Upload data to container
2. Prepare data by running the following gears:
   1. file metadata importer
   2. file classifier
   3. dcm2niix
3. Run the ciso gear (Hyperfine triplane aquisitions)
4. Run N4 bias correction gear
5. Run HD-BET
6. Run VBM

### Use Cases

## FAQ

[FAQ.md](FAQ.md)

## Contributing

[For more information about how to get started contributing to that gear,
checkout [CONTRIBUTING.md](CONTRIBUTING.md).]
