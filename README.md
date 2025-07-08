# SocialLLM

*CharacterBench-compatible tools for evaluating the social-interactive quality of large language models.*

SocialLLM collects **prompt templates, scoring guidelines, and turnkey scripts** that make it easy to **benchmark chat models on two core social abilities**:

| Sub-benchmark              | What it measures                                                    | Guideline file                                               |
| -------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Human Likeness**         | How lifelike and personality-consistent a model’s reply feels       | `human_likeness.py` ([raw.githubusercontent.com][1])         |
| **Emotion Self-Awareness** | Whether the model correctly perceives and mirrors a user’s emotions | `emotion_self_awareness.py` ([raw.githubusercontent.com][2]) |

The project was originally built for **\[AAAI] Tsinghua CoAI’s CharacterBench** and can be adapted to any JSONL dialogue dataset.
```text
SocialLLM
│
├── emotion_self_awareness.py
├── human_likeness.py
├── evaluation_prompt.py
├── inference.py
├── inference_base.py
└── emotion_self_awareness_benchmark_data_sample.json
```
---

## Features

* **Ready-made evaluation guidelines** – detailed, rubric-driven scoring instructions you can feed directly to an LLM judge.
* **Plug-and-play inference pipeline** – example scripts (`inference.py`, `inference_base.py`) showing how to batch-query OpenAI-compatible endpoints. ([raw.githubusercontent.com][3], [raw.githubusercontent.com][4])
* **Sample dataset** – `emotion_self_awareness_benchmark_data_sample.json` demonstrates the expected data format. ([raw.githubusercontent.com][5])
* **Easily extensible** – add new social skills by dropping in a guideline file and updating `evaluation_prompt.py`.

---

## Quick Start

### 1 · Install

```bash
git clone https://github.com/XMZhangAI/SocialLLM.git
cd SocialLLM
python3 -m venv .venv && source .venv/bin/activate
pip install openai httpx  # plus any other dependencies you prefer
```

> **Tip:** set your `OPENAI_API_KEY` (or compatible) as an environment variable.

### 2 · Prepare data

Each line of the input **JSONL** file should look like:

```jsonc
{
  "character_profile": "...",
  "dialogue": [
    {"turn": 1, "speaker": "user",      "utterance": "..."},
    {"turn": 1, "speaker": "character", "utterance": "..."}
    // ...
  ],
  "response_messages": { "response": "..." }
}
```

A small sample lives in `emotion_self_awareness_benchmark_data_sample.json`.

### 3 · Run inference

```bash
python inference.py \
    --input  emotion_self_awareness_benchmark_data_sample.json \
    --model  gpt-4o-mini           # or any chat-completion model
```

The script will:

1. Load the dataset
2. Build an **evaluation prompt** combining the character profile, dialogue context, and response
3. Query your chosen model endpoint
4. Print the raw model output for later scoring

### 4 · Score outputs

Feed each model reply, together with the original context, into the corresponding **judge prompt** defined in the guideline files (`Human_Likeness_Judge_Prompt`, `Emotion_Self_Awareness_Judge_Prompt`).
A second-pass “double-check” prompt is also provided to catch rubric drift and hallucinated scores.

---

## Repository Layout

| Path                                                | Purpose                                                      |
| --------------------------------------------------- | ------------------------------------------------------------ |
| `emotion_self_awareness.py`                         | Full scoring rubric + single- and double-check judge prompts |
| `human_likeness.py`                                 | Scoring rubric + judge prompts for human-likeness            |
| `evaluation_prompt.py`                              | (stub) utility for building task prompts                     |
| `inference.py`                                      | Example batch inference with OpenAI-style API                |
| `inference_base.py`                                 | Minimal end-to-end demo call                                 |
| `emotion_self_awareness_benchmark_data_sample.json` | Example data (truncated sample)                              |

---

## Extending SocialLLM

1. **Create a new rubric**
   Duplicate one of the guideline files and write a clear step-by-step rubric (`*_Guideline`) plus judge prompts (`*_Judge_Prompt`, `Double_Check_*`).
2. **Update `evaluation_prompt.py`**
   Add a function that assembles the user dialogue + candidate response into a single evaluation prompt.
3. **Benchmark**
   Plug the new prompts into your evaluation harness (LLM-as-Judge, human annotators, etc.).

---

## Citation

If you build on SocialLLM, please cite the MetaMind paper and this repository:

```bibtex
@article{zhang2025metamind,
  title={MetaMind: Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems},
  author={Zhang, Xuanming and Chen, Yuxuan and Yeh, Min-Hsuan and Li, Yixuan},
  journal={arXiv preprint arXiv:2505.18943},
  year={2025}
}

@misc{socialllm2025,
  title   = {SocialLLM: CharacterBench-Compatible Evaluation Prompts for Social LLMs},
  author  = {Zhang, Xuanming},
  howpublished = {\url{https://github.com/XMZhangAI/SocialLLM}},
  year    = {2025}
}
```

---

## License

This work is released under the **MIT License** unless noted otherwise in individual files.

---

## Acknowledgements

*Built and maintained by **XMZhangAI**. Inspired by the CoAI-Tsinghua CharacterBench project.*

[1]: https://raw.githubusercontent.com/XMZhangAI/SocialLLM/main/human_likeness.py "raw.githubusercontent.com"
[2]: https://raw.githubusercontent.com/XMZhangAI/SocialLLM/main/emotion_self_awareness.py "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/XMZhangAI/SocialLLM/main/inference.py "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/XMZhangAI/SocialLLM/main/inference_base.py "raw.githubusercontent.com"
[5]: https://raw.githubusercontent.com/XMZhangAI/SocialLLM/main/emotion_self_awareness_benchmark_data_sample.json "raw.githubusercontent.com"
