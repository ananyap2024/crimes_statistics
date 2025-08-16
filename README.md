
# 📊 Crime Statistics Visualization Tool 

### Description

This is a Python-based interactive CLI tool that visualizes crime records across 20 Indian states for the years **2019** and **2020**. It includes multiple crime categories and comparative analysis across years. Data visualization is done using `matplotlib`.

The program uses CSV files for data storage and offers users several plotting options (bar charts, pie charts, line plots, etc.) to understand crime trends better.

---

### 📁 Features

* **Interactive CLI** to explore crime datasets.
* **Visual representations** for:

  * Crime against children
  * Crime against women
  * Human trafficking
  * Crimes committed by juveniles
  * Total crime rates from 2000–2020
* Year-wise comparisons for 2019 and 2020.
* Support for multiple chart types (pie, bar, line, stem, step).
* CSV file-based input for extensibility.

---

### 🗂️ Directory Structure

```
project-root/
│
├── crime_against_children.csv
├── Crime Committed by Juveniles.csv
├── crime rates over the years 2000-2020.csv
├── main.py
├── README.md
└── other_crime_files.csv (used for categories 2 and 3)
```

> ⚠️ All CSV files are expected to be located in the path as defined in the code or updated accordingly.

---


---

### 🧭 CLI Command Guide

| Command       | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| `1`           | Show pie chart of **crime against children** for 2019 or 2020             |
| `1A`          | Show bar chart comparison of **crime against children** for 2019 and 2020 |
| `2`           | Show bar chart of **crime against women** for 2019 or 2020                |
| `2A`          | Show line plot comparison of **crime against women**                      |
| `3`           | Show stem plot of **human trafficking** cases                             |
| `3A`          | Compare human trafficking cases over years                                |
| `4`           | Show step plot of **crimes by juveniles**                                 |
| `4A`          | Bar chart comparison of **juvenile crimes**                               |
| `5`           | Line chart of **total crime rate** from 2000–2020                         |
| `h` or `help` | Show help text                                                            |
| `q` or `quit` | Exit the program                                                          |

---

### 🧾 Notes

* **CSV Format Assumption:** All datasets should contain at least `State`, `2019`, and `2020` columns.
* **Graph Labels:** Most graphs use states on the x-axis and number of cases on the y-axis.
* Ensure proper formatting of CSVs to avoid data parsing issues.
* **Easter Egg:** Entering `2025` under human trafficking category prints a cryptic message – possibly for future use or fun.

---

### 🧑‍💻 Author

**Ananya**
This tool was created as an educational and analytical project to visualize crime data using Python.

---

### 📌 Future Improvements

* Load data dynamically instead of hardcoded paths.
* Add a GUI using `Tkinter` or `PyQt`.
* Extend analysis to more years and more crime categories.
* Add data validation and error handling.

---

### 📜 License

This project is intended for educational use. Please contact the author for permission before using it commercially.

---
