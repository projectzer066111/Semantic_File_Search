# Local-First CLI File Search Engine

A high-performance, privacy-first local file search engine built from scratch in Python. Designed to run completely offline with zero cloud dependencies, leveraging SQLite's Full-Text Search (FTS5) to achieve sub-millisecond keyword retrieval across thousands of local files.

## 🚀 Key Engineering Features

* **Lightning-Fast Inverted Indexing:** Utilizes SQLite's `FTS5` virtual table extension to index filenames and custom tags, allowing for instant keyword and wildcard matching.
* **Database Optimization:** 
  * Implemented batched SQL transactions (`executemany()`) to maximize ingestion throughput during directory crawls.
  * Applied `UNINDEXED` constraints on metadata columns (like `filepath`) to optimize resource consumption and reduce database overhead.
* **Interactive CLI & State Caching:** Features a persistent terminal loop with runtime result-caching, enabling users to instantly open target files via native OS process execution (`os.startfile`).
* **100% Privacy-First:** Operates completely air-gapped with no telemetry, internet connectivity, or external servers required.

---

## 🛠️ Project Architecture

The codebase is split into modular utility scripts to separate indexing, database maintenance, and search operations:

1. **`indexer.py`** — Recursively crawls target directories using `os.walk`, filters system clutter, and batch-inserts paths into the SQLite database.
2. **`search.py`** — An interactive command-line search engine that interfaces with FTS5, ranks results, manages session state arrays, and triggers native file handlers.
3. **`resetdb.py`** — A database maintenance utility that clears records while preserving the optimized FTS5 virtual table schema.

---


## WIP
Currently the Opening of files when the results are returned isnt coded in yet. Will do so in my free time. For now it a super fast file searching system that returns the file and filepath.

## 💻 Getting Started

### Prerequisites
* Python 3.10+ (No external third-party pip packages required for core search/indexing!)

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name