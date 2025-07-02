# Project_LLM_A3

## TO-DO
    - Compilare i json
    - Compilare le tabelle
    - Scrivere i i paragrafi su OverLeaf 
    

## Cose Fatte

| App            | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|----------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| PassAndroid    |      RM       |          GM           |        RM        |           RM              |      MR       |          GM            |       RM         |
| TFA pre-log    |      X        |          X            |        RM        |           X               |      MR       |          GM            |       RM         |
| TFA post-log   |      GM       |          GM           |        RM        |           RM              |      RM       |          X            |       RM         |
| Omni-Notes     |      MR       |          GM           |        RM        |           RM              |      MR       |          GM            |       RM         |


Activity coverage e Valid set text in frazioni 

## PassAndroid

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |      110      |          110          |       214        |           77              |      170      |          170           |      119         |
| UTG edge            |      200      |          200          |       2087       |           232             |      360      |          360           |      230         |
| Activity coverage   |      4/15     |          4/15         |       4/15       |           5/15            |      4/15     |          4/15          |      5/15        |
| Valid set text      |      0/66     |          0/66         |       0/31       |           7/182           |      0/224    |          0/224         |      8/289       |

## TFA pre-log

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |      21       |          24           |       27         |           29              |      23       |          25            |      28          |
| UTG edge            |      32       |          35           |       38         |           40              |      34       |          36            |      39          |
| Activity coverage   |      55       |          58           |       60         |           63              |      57       |          59            |      62          |
| Valid set text      |      13       |          15           |       17         |           19              |      14       |          16            |      18          |

## TFA post-log

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |      31       |          34           |       37         |           39              |      33       |          35            |      38          |
| UTG edge            |      42       |          45           |       48         |           50              |      44       |          46            |      49          |
| Activity coverage   |      65       |          68           |       70         |           73              |      67       |          69            |      72          |
| Valid set text      |      18       |          20           |       22         |           24              |      19       |          21            |      23          |

## Omni-Notes

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG states           |      73       |          73           |       296         |           18              |      169       |          169            |      52          |
| UTG edges            |      173       |          173           |       787         |           32              |      419       |          419            |      125          |
| Activity coverage   |      3/15       |          3/15           |       2/15         |           1/15              |      5/15       |          5/15            |      3/15          |
| Valid set text      |      80.65% (50/62)       |          38.71% (24/62)           |       80.65% (25/31)         |           36.47% (31/85)              |      52.91% (91/172)       |          58.14% (100/172)           |       46.84% (74/158)          |

Note: the 'Humanoid base' folder is hidden because it exceeds 100 MB and is included in the .gitignore file.

## Limitazioni

Elenco dei motivi per cui si potrebbero migliorare i risultati:
    - HW e Risorse
    - Più tempo di test
    - Codice del app poco descrittivo nei componenti, poichè il contesto è derivato da quello, se poco esplicativi, il modello ha poche info per essere più accurato.
    - Più app. 
