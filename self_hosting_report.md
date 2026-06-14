## Task 1 — Benchmark two local models

Same prompt for both. Get RAM from your OS activity monitor / `top`.

| Model          | Approx size / quant | Load time (s) | Tokens/sec | RAM used | Quality note                                                                                                                                    |
| -------------- | ------------------- | ------------- | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `llama3.2:3b`  | 3B / Q4_K_M         | 1.89          | 70.85      | ~914 MB  | Produced a concise and coherent answer with a relevant example, though it contained a technical inaccuracy about fine-tuning during generation. |
| `qwen2.5:0.5b` | 0.5B / Q4_K_M       | 0.08          | 229.71     | ~719 MB  | Generated a longer response with multiple examples, but included redundant information and several inaccuracies about how RAG works.            |

**Trade-off you observed (2–3 sentences):**

> The smaller `qwen2.5:0.5b` model generated responses over three times faster while using less memory, making it well suited for lightweight local inference. However, `llama3.2:3b` produced a more coherent and focused explanation, despite generating responses more slowly. This benchmark demonstrates the typical trade-off between inference speed and response quality when comparing smaller and larger language models.

## Task 3 — VLM: local vs hosted

Image used: `sample_chart.png` (provided).
Task performed: Chart description and OCR.

| System                | Answer (short)                                                                                                                                                | Speed  | Cost         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------ |
| Local VLM (Moondream) | Correctly identified the image as a bar chart comparing inference speed, but made several OCR errors and failed to accurately extract model names and values. | ~2–3 s | Free / local |
| Gemini (multimodal)   | Correctly identified the chart title, subtitle, axis labels, model names, parameter sizes, numerical values, and summarized the overall trend.                | ~1–2 s | Free tier    |

**Comparison (2–3 sentences):**

> Moondream was able to recognize the overall structure and purpose of the chart, but its OCR accuracy was limited, causing incorrect model names and missing numerical details. Gemini produced a much more accurate analysis by correctly reading the chart text and extracting the quantitative information. While the local model has the advantage of running offline at no cost, the hosted model provided noticeably higher quality for chart understanding and OCR.
