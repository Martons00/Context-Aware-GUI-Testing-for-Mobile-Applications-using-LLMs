# Struttura Presentazione PowerPoint: Context-Aware GUI Testing con LLMs
## Versione Enumerata e Organizzata

### **Slide 1: Titolo** *(30 secondi)*
**Contenuto:**
- **Titolo principale**: Context-Aware GUI Testing for Mobile Applications with LLMs
- **Sottotitolo**: Un approccio sistematico con 7 configurazioni di testing
- **Autori**: Raffaele Martone, Michele Russo, Giuseppe Monteasi
- **Data e contesto**: Progetto di Machine Learning Applications - Luglio 2025

### **Slide 2: Il Problema Centrale** *(1 minuto)*
**Contenuto:**
- **Headline**: "I framework di testing mobile tradizionali hanno un limite critico"
- **Problema principale**: 
  - DroidBot e Humanoid inseriscono solo "Hello World" nei campi di testo
  - Impossibilità di superare schermate che richiedono input specifici
  - Copertura limitata delle funzionalità reali delle app
- **Visual suggerito**: Screenshot side-by-side di un form con "Hello World" vs form compilato correttamente

### **Slide 3: Research Questions** *(30 secondi)*
**Contenuto:**
- **RQ1**: How effectively can LLMs generate working context-aware test cases for mobile GUI testing?
- **RQ2**: What coverage can be obtained by generating test cases with LLMs?
- **Focus**: Misurare effectiveness (test funzionanti) vs coverage (stati esplorati)

### **Slide 4: Metodologia - Le 7 Configurazioni** *(2 minuti)*
**Contenuto:**
- **Baseline** (2): DroidBot base, Humanoid base
- **Replay-Enhanced** (2): + Replay output (approccio offline)
- **LLM-Enhanced** (3): + LLAMA text, + LLAMA + Choice, + Humanoid + LLAMA
- **3 App testate**: PassAndroid (gestione pass digitali), Omni-Notes (note-taking), Thunderbird Android (email)
- **Visual suggerito**: Diagramma a flusso che mostra l'evoluzione dalle configurazioni base a quelle LLM-enhanced

### **Slide 5: Integrazione LLM - Due Approcci** *(1.5 minuti)*
**Contenuto:**
- **Approccio Offline (Replay)**: 
  - Post-processing dei file JSON di DroidBot
  - Sostituzione "Hello World" con testi contestuali
  - Ri-esecuzione dei test modificati
- **Approccio Online (Real-time)**:
  - Integrazione diretta nel codice di DroidBot/Humanoid
  - Generazione dinamica durante l'esplorazione
  - Prompt engineering con few-shot learning
- **Visual suggerito**: Schema architetturale che mostra i due flussi

### **Slide 6: Prompt Engineering - Esempi Concreti** *(1 minuto)*
**Contenuto:**
- **Text Generation Prompt** (esempio ridotto):
```
You are an assistant that generates context-aware text inputs.
[UI Representation]
Enter email
Output: john.doe@example.com
```
- **Action Selection Prompt** (esempio ridotto):
```
Given UI state and possible actions, select appropriate index.
Example: Given email form and buttons [0,1,2], Output: 1
```
- **Strategia**: Few-shot learning + contesto dinamico

### **Slide 7: Risultati PassAndroid - Tabella Generale** *(2 minuti)*
**Contenuto:**
- **Tabella completa dei risultati**:
  
| Configurazione | UTG State | UTG Edge | Activity Coverage | Valid Set Text |
|---------------|-----------|----------|-------------------|----------------|
| DroidBot base | 110 | 200 | 4/15 | 0/66 |
| DroidBot + Replay | 110 | 200 | 4/15 | 0/66 |
| DroidBot + LLAMA | 214 | 2087 | 4/15 | 0/31 |
| DroidBot + LLAMA + Choice | 77 | 232 | **5/15** | **7/182** |
| Humanoid base | 170 | 360 | 4/15 | 0/224 |
| Humanoid + Replay | 170 | 360 | 4/15 | 0/224 |
| Humanoid + LLAMA | 119 | 230 | **5/15** | **8/289** |

- **Insight chiave**: Solo le configurazioni con decision-making (Choice) mostrano miglioramenti reali

### **Slide 8: Risultati Thunderbird Android - Tabella Generale** *(2 minuti)*
**Contenuto:**
- **Tabella dei risultati per TFA**
- **Confronto delle metriche tra le 7 configurazioni**
- **Analisi specifica per client email**
- **Comportamenti osservati nella gestione account e autenticazione**

### **Slide 9: Risultati Omni-Notes - Tabella Generale** *(2 minuti)*
**Contenuto:**
- **Tabella dei risultati per Omni-Notes**
- **Confronto delle metriche tra le 7 configurazioni**
- **Analisi specifica per app note-taking**
- **Comportamenti osservati nella gestione note e reminder**

### **Slide 10: RQ1 - Effectiveness Analysis** *(2 minuti)*
**Contenuto:**
- **Finding principale**: La sola generazione di testo non basta
- **Valid Set Text** - Solo successi con:
  - DroidBot + LLAMA + Choice: 7/182 (3.8%)
  - Humanoid + LLAMA: 8/289 (2.8%)
- **Insight critico**: Il decision-making intelligente è cruciale quanto la generazione di testo
- **Visual suggerito**: Grafico a barre che evidenzia i Valid Set Text per configurazione

### **Slide 11: RQ2 - Coverage Analysis** *(2 minuti)*
**Contenuto:**
- **Activity Coverage**: Miglioramento marginale da 4/15 a 5/15
- **UTG States/Edges**: LLAMA text generation causa esplosione di transizioni (2087 vs 200-360)
- **Trade-off identificato**: Più esplorazione ≠ necessariamente più effectiveness
- **Limitazioni**: UI Automator difficoltà con hamburger menu, caricamento file esterni
- **Visual suggerito**: Grafico dual-axis che mostra exploration vs effectiveness

### **Slide 12: Limitazioni e Sfide Identificate** *(1.5 minuti)*
**Contenuto:**
- **Limitazioni Tecniche**:
  - Risorse computazionali limitate (tempo/hardware)
  - Descriptiveness scarsa del codice delle app testate
  - Sample size ridotto (3 app)
- **Limitazioni Architetturali**:
  - UI Automator vs elementi complessi (hamburger menu)
  - Impossibilità caricamento file esterni (storage/camera)
- **Implicazione**: Framework tradizionali restano limitanti anche con LLM

### **Slide 13: Discussione - LLM vs Manual Testing** *(1.5 minuti)*
**Contenuto:**
- **Vantaggi LLM-based**:
  - ✅ Automazione e scalabilità
  - ✅ Input contestuali realistici
  - ✅ Esplorazione più profonda
- **Limitazioni attuali**:
  - ❌ Non risolve completamente il problema
  - ❌ Dipende dalla qualità del contesto disponibile
  - ❌ Effectiveness ancora limitata
- **Conclusione**: Approccio promettente ma necessita raffinamenti

### **Slide 14: Conclusioni e Contributi** *(1 minuto)*
**Contenuto:**
- **Key Findings**:
  - Decision-making è cruciale quanto text generation
  - LLM migliorano exploration ma effectiveness resta limitata
  - Trade-off tra quantità esplorazione e qualità test
- **Contributo Scientifico**: Primo studio sistematico su 7 configurazioni LLM per GUI testing mobile
- **Future Work**: Hardware migliore, più app, tempi esecuzione estesi
- **Impatto**: Fondamenta per framework intelligenti di testing

### **Slide 15: Q&A**
**Contenuto:**
- **Thank you for your attention**
- **Questions?**
- **Contatti** (opzionale)


| Slide | Titolo                                      | Chi la discute |
|-------|---------------------------------------------|----------------|
| 1     | Titolo                                      |   MR           |
| 2     | Il Problema Centrale                        |   MR           |
| 3     | Research Questions                          |   MR           |
| 4     | Metodologia - Le 7 Configurazioni tranne LLM|   MR           |
| 4     | Metodologia - Le 7 Configurazioni LLM       |   RM           |
| 5     | Integrazione LLM - Due Approcci             |   RM           |
| 6     | Prompt Engineering - Esempi Concreti        |   RM           |
| 7     | Risultati PassAndroid - Tabella Generale    |   RM           |
| 8     | Risultati Thunderbird Android - Tabella     |   GM           |
| 9     | Risultati Omni-Notes - Tabella              |   GM           |
| 10    | RQ1 - Effectiveness Analysis                |   GM           |
| 11    | RQ2 - Coverage Analysis                     |   GM           |
| 12    | Limitazioni e Sfide Identificate            |   GM           |
| 13    | Discussione - LLM vs Manual Testing         |   GM           |
| 14    | Conclusioni e Contributi                    |   *            |
| 15    | Q&A                                         |   *            |
