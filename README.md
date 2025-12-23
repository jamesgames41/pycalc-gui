# PyCalc GUI: Graphical Python Calculator

PyCalc GUI is the evolution of the [original PyCalc](https://github.com/jamesgames41/pycalc) project. It transforms the lightweight CLI calculator into a user-friendly desktop application using Python's **Tkinter** library. 

Whether you need to perform quick arithmetic or solve geometric problems, PyCalc GUI provides a clean, tabbed interface to handle calculations without using the terminal.

---

## ✨ Features

PyCalc GUI organizes its functionality into three dedicated tabs for easy navigation:

### 1. Basic Arithmetic
* **Operations**: Supports addition, subtraction, multiplication, and division.
* **Input Validation**: Includes error handling for non-numeric inputs and prevents division by zero.

### 2. 2D Geometry (Area)
Quickly calculate the area for common shapes:
* **Rectangle / Square**: Calculated via Length × Width.
* **Circle**: Calculated using $\pi r^2$.
* **Triangle**: Calculated via (Base × Height) / 2.

### 3. 3D Geometry
Support for volume and surface area computations based on the original logic:
* **Cube**: Calculates Surface Area (Edge² × 6).
* **Sphere**: Calculates Surface Area ($4\pi r^2$).
* **Rectangular Prism**: Calculates Volume (Length × Width × Height).

---

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/jamesgames41/pycalc-gui.git](https://github.com/jamesgames41/pycalc-gui.git)
    ```
2.  **Navigate to the directory**:
    ```bash
    cd pycalc-gui
    ```
3.  **Run the application**:
    ```bash
    python gui_launcher.py
    ```
    *(Note: Ensure you have Python installed. Tkinter is typically included with standard Python installations.)*

---

## 🖥️ Usage

1. **Launch**: Run `gui_launcher.py` to open the main window.
2. **Select Mode**: Use the tabs at the top (Basic Calc, 2D Shapes, or 3D Shapes) to choose your calculator type.
3. **Calculate**: Enter your values into the provided fields and click the **Calculate** button to see the result instantly.

---

## 🔄 Relationship to Original PyCalc
This project is based on the logic developed for the original **PyCalc** CLI application. While the original used terminal-based prompts and separate scripts for each mode, **PyCalc GUI** centralizes all logic into a single graphical interface.

---

## 🤝 Contributing
Contributions are welcome! If you want to add more shapes or improve the UI:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewShape`).
3. Commit your Changes.
4. Push to the Branch.
5. Open a Pull Request.
