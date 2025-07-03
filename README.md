# Context-Aware GUI Testing for Mobile Applications using LLMs

[![GitHub Repository](https://img.shields.io/badge/GitHub-Project_LLM_A3-blue)](https://github.com/Martons00/Project_LLM_A3)

This repository contains the complete research materials, experimental data, and analysis scripts for the project "Context-Aware GUI Testing for Mobile Applications using Large Language Models (LLMs)".

## 📋 Project Overview

This research investigates the potential of Large Language Models (LLMs) to enhance context-aware GUI testing in mobile applications. The study focuses on improving test coverage and generating more realistic, contextually appropriate test cases by integrating LLMs with traditional automated testing frameworks.


## 📄 Documentation

- **Complete Report**: [`LLM_Project_A3_Final_Report.pdf`](./LLM_Project_A3_Final_Report.pdf)
- **Presentation**: [`LLM_Project_A3_Final_PPT.pdf`](./LLM_Project_A3_Final_PPT.pdf)

### Research Questions

- **RQ1**: How effectively can LLMs generate working context-aware test cases for mobile GUI testing?
- **RQ2**: What coverage can be obtained by generating test cases with LLMs?

### Authors
- **Raffaele Martone**
- **Michele Russo** 
- **Giuseppe Monteasi**

*Date: July 6, 2025*

## 🚀 Key Contributions

- Integration of LLAMA with DroidBot and Humanoid testing frameworks
- Context-aware text input generation using prompt engineering techniques
- Strategic decision-making for action selection in GUI exploration
- Comprehensive evaluation across multiple Android applications
- Analysis of both offline (replay) and online (real-time) LLM integration approaches

## 📁 Repository Structure

```
Project_LLM_A3/
├── Papers/                          # Reference papers and related work
│   ├── DroidBot_a_lightweight_UI-Guided_test_input_generator_for_android.pdf
│   ├── Humanoid.pdf
│   ├── GPTDroid.pdf
│   ├── DROIDFILLER.pdf
│   ├── Fill in the Blank.pdf
│   ├── Survey Testing.pdf
│   └── Projects-LLM-8-10.pdf
├── Result/                          # Experimental results organized by configuration
│   ├── 00-Droidbot Base/
│   ├── 01-Droidbot Replay Output/
│   ├── 02-Droidbot + LLAMA/
│   ├── 03-Droidbot + LLAMA + Scelta/
│   ├── 04-Humanoid Base/
│   ├── 05-Humanoid + Replay Output/
│   └── 06-Humanoid + LLAMA/
├── Script/                          # Analysis and data processing scripts
│   ├── Correction_stats.ipynb      # Statistical analysis and corrections
│   ├── Extract_info_from_json.ipynb # JSON data extraction utilities
│   └── Replay_output_LLM.ipynb              # LLM integration scripts
├── LLM_Project_A3_Final_Report.pdf # Complete research report
├── LLM_Project_A3_Final_PPT.pdf    # Project presentation
└── README.md                       # This file
```

## 🧪 Experimental Setup

### Testing Frameworks

#### **DroidBot**
- Lightweight, open-source tool for automated test input generation
- Builds dynamic state transition models during app execution
- Depth-first exploration strategy for comprehensive coverage

Droidbot Repo LLAMA Integration: https://github.com/Martons00/droidbot/tree/LLama_Integration

#### **Humanoid**
- Advanced input generator using deep learning
- Trained on hundreds of thousands of human interaction traces (Rico dataset)
- Predicts user-likely UI element selections and actions

### LLM Integration Approaches

1. **Baseline Approaches**
   - DroidBot base: Standard automatic GUI exploration
   - Humanoid base: Deep learning-based human interaction simulation

2. **Replay-Enhanced Approaches**
   - DroidBot + Replay: Offline LLM post-processing of JSON outputs
   - Humanoid + Replay: Combination of Humanoid exploration with LLM text processing

3. **LLM-Enhanced Approaches**
   - DroidBot + LLAMA: Real-time text generation during exploration
   - DroidBot + LLAMA + Choice: Text generation + strategic action selection
   - Humanoid + LLAMA: Humanoid exploration with LLM text generation

### Target Applications

#### **PassAndroid**
- Open-source digital pass manager (tickets, loyalty cards, coupons)
- Complex form interactions and barcode management
- Dynamic data handling and sharing functionalities

#### **Omni-Notes**
- Note and task management application
- Rich interactive widgets and navigation flows
- Advanced features: categorization, search, reminders, multimedia attachments

#### **Thunderbird Android (TFA)**
- Open-source email client with privacy focus
- Complex pre-login and post-login scenarios
- Multi-account management and advanced email functionalities

## 📊 Key Results

### Summary Metrics

| Application | Best Configuration | Activity Coverage | Valid Text Inputs |
|-------------|-------------------|-------------------|-------------------|
| **PassAndroid** | DroidBot + LLAMA + Choice / Humanoid + LLAMA | 5/15 (33.3%) | 7-8/182-289 |
| **TFA Post-Login** | Humanoid + LLAMA | 2/28 | 27/28 (96.4%) |
| **Omni-Notes** | Humanoid base/Replay | 5/15 (33.3%) | 91-100/172 (52-58%) |

### Key Findings

- **Context Quality Impact**: LLM effectiveness strongly correlates with the richness of contextual information available
- **Strategic Decision-Making**: Configurations using LLMs for action selection show improved activity coverage
- **Text Generation**: LLM-enhanced approaches generate more diverse and contextually appropriate inputs
- **Application Dependency**: Performance varies significantly based on app architecture and metadata quality

## 🔧 Usage

### Prerequisites
- Python 3.x with Jupyter Notebook support
- Android development environment
- Access to LLAMA model (local or API)
- Target Android applications (APKs)

### Running Experiments

1. **Setup Environment**:
   ```bash
   git clone https://github.com/Martons00/Project_LLM_A3.git
   cd Project_LLM_A3
   ```

2. **Data Analysis**:
   ```bash
   jupyter notebook Script/Correction_stats.ipynb
   ```

3. **Extract Results**:
   ```bash
   jupyter notebook Script/Extract_info_from_json.ipynb
   ```

### Result Analysis Scripts

- **`Correction_stats.ipynb`**: Statistical analysis and data corrections
- **`Extract_info_from_json.ipynb`**: Utilities for extracting information from test execution logs
- **`Replay_output_LLM.ipynb`**: LLM integration and processing scripts

## 📈 Metrics Explained

### Coverage Metrics
- **UTG State**: Number of unique UI states discovered
- **UTG Edge**: Number of state transitions recorded
- **Activity Coverage**: Ratio of app activities reached vs. total activities

### Effectiveness Metrics
- **Valid Set Text**: Ratio of semantically correct text inputs vs. total text input attempts
- **Success Rate**: Percentage of test cases that execute successfully

## ⚠️ Limitations

Current limitations that affect the experimental results:

1. **Hardware Constraints**: Limited computational resources restrict extensive exploration
2. **Time Constraints**: Short test execution windows limit state discovery
3. **Code Descriptiveness**: Poor app metadata quality reduces LLM context effectiveness
4. **Sample Size**: Limited to three applications, affecting generalizability

## 🔮 Future Work

### Immediate Improvements
- Scale experiments with more powerful hardware
- Extend test execution time windows
- Expand evaluation to larger, more diverse app sets

### Advanced Techniques
- Enhanced context extraction methods
- Better app documentation standards
- Advanced prompt engineering strategies
- Multi-modal context integration

## 📚 References

The `Papers/` directory contains all relevant research papers that informed this work, including:

- DroidBot framework documentation
- Humanoid deep learning approach
- GPTDroid functionality-aware testing
- DroidFiller context-aware text generation
- Comprehensive survey on LLMs in software testing


## 🤝 Contributing

This repository represents completed research work. For questions or discussions about the methodology or results, please open an issue or contact the authors.

## 📧 Contact

For inquiries about this research project, please contact the authors through their institutional affiliations or via GitHub issues.

---

**Note**: Some large result files (>100MB) are excluded via `.gitignore` for repository size management. Complete datasets are available upon request.