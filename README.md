# Infer masked token with BERT

## Introduction

BERT, or Bidirectional Encoder Representations from Transformers, is a new method of pre-training language representations which obtains state-of-the-art results on a wide array of Natural Language Processing (NLP) tasks.

In order to train a deep bidirectional representation in BERT, the authors  masked some input tokens randomly, and then predict those masked tokens. This procedure is known as a **masked LM** (MLM).

In this repository, I have implemented **a basic script to infer the masked token** in a sentence.

Read the BERT paper: https://arxiv.org/pdf/1810.04805.pdf

## Code

With this repository, there are some commands in Bash to run the Python code in a Docker container. Anyway, you can find all the Python scripts at [./code](./code)

You can see the code execution step by step in the notebooks (see folder [./notebooks](./notebooks)). Additionally, the notebooks are available at Kaggle:
- https://www.kaggle.com/dimasmunoz/infer-masked-token-with-bert

## Commands

> Note: These commands have been tested in MacOS and Git Bash (Windows).

You can start/stop the docker container with these two commands:
```sh
sh manager.sh docker:run
sh manager.sh docker:down
```

Once the docker container is running, execute the BERT script as follows:
```sh
sh manager.sh bert
```

Then, it will display a prompt where you can write your sentences with a masked token. For example:
```
$ sh manager.sh bert
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 996k/996k [00:02<00:00, 485kB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 625/625 [00:00<00:00, 176kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 714M/714M [01:07<00:00, 10.7MB/s]

Input text: This is a [MASK] model
----------------------------------------
mathematical 0.04100513085722923
model 0.03972144424915314
single 0.01666860282421112
similar 0.014901496469974518
common 0.01419056300073862
========================================

...
```

Have fun! ᕙ (° ~ ° ~)
