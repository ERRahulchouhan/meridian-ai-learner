# 15 · What you need: skills, accounts, software, costs

---

## 1. Skills

| You should know | How well |
|---|---|
| Python | Functions, classes, packages, virtual environments |
| **LangChain basics** | Prompts, chat models, chains, what a tool is |
| Command line | Run commands, set environment variables |
| Git | Clone a repository |

You do **not** need cloud, FastAPI, Docker or CI/CD experience. This guide explains them.

## 2. Accounts

| Account | Needed for | Cost | Path |
|---|---|---|---|
| **Google account** | All Google things | Free | all |
| **OpenAI API key** (https://platform.openai.com/api-keys) | Chat model and local embeddings | Usage-based pricing | all |
| **Google Cloud account** | Vector database, storage, hosting | **$300 free credit** for new customers | cloud |
| **GitHub account** | Robot that sets up and deploys | Free | cloud |

A **card is required** for Google Cloud, even for the free trial. Google places a temporary hold to check it; it is not a charge.

### OpenAI API key
- Create a key at https://platform.openai.com/api-keys.
- API usage is billed according to the selected models; check current rates at https://openai.com/api/pricing/.
- The chat model and local-mode embeddings use the OpenAI API. Cloud-mode embeddings continue to use Vertex AI.

### The $300 Google Cloud credit
| Question | Answer |
|---|---|
| How much? | **$300** |
| For how long? | **90 days** (about three months) |
| Who? | **New customers only** |
| Card? | Yes (hold, not charge) |
| Automatic charge after? | **No**; only if you upgrade |
| When it ends | At 90 days **or** $300 used, whichever first. After a 30-day grace period, trial resources are **deleted** |
| Limits | Some generative-AI services are restricted; people report tight limits on trial accounts. The chat model uses your OpenAI key, while cloud-mode **embeddings** run on Google Cloud and could be limited. If you see "project is not allowed…", upgrade to the full account (credit is still used first) |

Source: https://docs.cloud.google.com/free/docs/free-cloud-features

## 3. Software

| Tool | Version | Used for |
|---|---|---|
| Python | 3.12 | Backend |
| Node.js + npm | 20+ | Frontend |
| Git | any recent | Getting the code |
| Google Cloud CLI (`gcloud`) | recent | Cloud setup (cloud path) |
| Docker Desktop | recent | Optional |
| A code editor (e.g. VS Code) | – | Reading and editing |

**Windows:** the commands use macOS/Linux style. **WSL 2** is the smoothest way to follow along.

Computer: 8 GB memory, 3 GB free disk, internet.

## 4. What costs money

| Service | Billed | Expect |
|---|---|---|
| **Vector Search** | **By the hour while deployed, even with no users** | **The main cost** |
| Cloud Run | Only when used | Usually inside the free monthly allowance |
| Cloud Storage, Cloud Build, Secret Manager | Tiny | Cents or free allowances |
| OpenAI API | Per token | Depends on model and usage |

**Vector Search warning.** The setup script does not choose a machine size or number of copies. Google's documentation says the number of copies defaults to **2**. A small machine is reported at about $0.08 an hour (roughly $56 a month) by third-party guides; that is not an official figure (https://cloud.google.com/vertex-ai/pricing). **Do your cloud work in one sitting and delete the database when you finish.** A **budget alert** only emails you; it does not stop spending.

Steps and the clean-up commands are in [DEPLOY.md](../DEPLOY.md).

## 5. Time

| Task | Time |
|---|---|
| Audit on your computer | about 10–30 minutes |
| Google Cloud setup | about 30–45 minutes |
| First cloud deployment | **30–45 minutes of waiting** |
| Reading this guide | 2–3 hours |

## 6. Checklist
- [ ] Google account
- [ ] OpenAI API key
- [ ] Python 3.12, Node.js 20+, Git
- [ ] (Cloud) Card, budget alert, `gcloud`, GitHub account
