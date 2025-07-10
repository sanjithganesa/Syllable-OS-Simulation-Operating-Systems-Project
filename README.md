# 🧠 Syllable OS Simulation – Operating Systems Project

This repository contains a comprehensive **simulation of Syllable OS internals**, designed as part of our Operating Systems coursework. The simulation models threading, process synchronization, memory management, disk partitioning, and file system operations, reflecting the design principles of the real-world [Syllable OS](https://syllable.metaproject.frl/).

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Implemented Modules](#implemented-modules)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [License](#license)

---

## 📌 Project Overview

Syllable OS is a lightweight, POSIX-compliant operating system built for desktop PCs. This project replicates some of its **core components** using modular code to demonstrate:

- Contiguous memory allocation strategies (First Fit & Best Fit)
- Threading simulation in a monolithic kernel model
- Device management and disk partitioning
- Process synchronization using semaphores and resource trees
- Page replacement algorithms (LRU & Optimal)
- File system operations with Linux-like structure
- CLI and GUI-based exploration of Syllable OS
- Comparison with Unix system calls

> The aim is to visualize and implement core OS concepts using an educational, modular simulation approach.

---

## ⚙️ Implemented Modules

| Module                  | Description |
|------------------------|-------------|
| ✅ Threading            | Simulated monolithic kernel-style threading using a `Kernel` class and locking mechanisms |
| ✅ Memory Management    | First Fit and Best Fit allocation within a contiguous memory model |
| ✅ Device Management    | Simulated `DeviceManager` with node creation, disk partitioning, renaming, and visualization |
| ✅ Process Sync         | Semaphore and resource tree system for lock management |
| ✅ Page Replacement     | LRU and Optimal algorithms with reference tracking and memory simulation |
| ✅ File Management      | Linux-like file system tree for navigating, reading, and writing files |
| ✅ System Call Mapping  | System call simulation for processes, files, memory, and IPC |
| ✅ Comparison           | Evaluation of Syllable vs Unix system calls and architecture advantages |

---

## 🛠 Technologies Used

- C++ / Python (depending on your code)
- Custom-built simulation logic
- CLI interface for input/output
- VMware Workstation or VirtualBox (for OS installation and testing)

---

## 🖼 Screenshots

### 📌 Review 1: Syllable OS Installation & Basics

| VMware Emulator | Syllable Boot Screen | Installation |
|-----------------|----------------------|--------------|
| ![vmware](https://github.com/user-attachments/assets/e2da2936-ad2a-43ba-84f8-2ee3427d9031) | ![boot](https://github.com/user-attachments/assets/ab87b2b4-ee77-4feb-abfc-5fb30e5a996e) | ![install](https://github.com/user-attachments/assets/9fb87bd8-c303-407f-9e59-88e0d9dc00b8) |

**Full Installation Process:**

![1](https://github.com/user-attachments/assets/b1f1c379-cd83-479f-9cd8-4e105ddbb7a4)  
![2](https://github.com/user-attachments/assets/708fbc2f-245d-456f-9186-29a184ac0bb7)  
![3](https://github.com/user-attachments/assets/c5320e16-c532-4075-8829-9777f0bd41d2)  
![4](https://github.com/user-attachments/assets/ea4a6a37-52bb-40f2-8beb-1776e6f2752b)  
![5](https://github.com/user-attachments/assets/fe65f7ce-b589-4f62-9b2e-ee0068515c24)  
![6](https://github.com/user-attachments/assets/01f3cb64-fd7a-4563-9e5b-263456173461)  
![7](https://github.com/user-attachments/assets/04e28f90-1eb2-4e93-827a-1f8611918711)  
![8](https://github.com/user-attachments/assets/0c78977e-5391-413e-9cce-12e4829dd82e)  
![9](https://github.com/user-attachments/assets/1efd7cd5-6368-4584-aa3e-ea9e71d6ecc4)

**Shell Command Execution:**

![cli1](https://github.com/user-attachments/assets/8c3acfd7-8131-4490-92eb-ff264979e732)  
![cli2](https://github.com/user-attachments/assets/90d1404b-9ddf-485d-b082-b495cb95d653)

**GUI Interface and Desktop Preview:**

![gui1](https://github.com/user-attachments/assets/40800a89-77e6-4ed5-93d0-9164de08c47d)  
![gui2](https://github.com/user-attachments/assets/45b1eaa2-f706-4e13-a4f9-8b33f00cbc27)

**System Calls Demonstration:**

![delight](https://github.com/user-attachments/assets/e909e1de-951d-46c1-8e3a-74259e4bd8f8)  
![delight-2](https://github.com/user-attachments/assets/cfdf28e6-38b4-4c3d-8971-4fdae98f7daf)  
![gcc](https://github.com/user-attachments/assets/ea73ed65-d5b6-46a1-997e-c8cde859696d)  
![syscall](https://github.com/user-attachments/assets/a15b1c3e-32f7-468c-8835-9b51331ec8b8)  
![syscall-log](https://github.com/user-attachments/assets/e460f2ee-18d2-450e-b3cf-1678137f26e7)

---

### 📌 Review 2: Internal Simulations & Kernel Features

In the second phase of the project, we focused on simulating the core internal functionalities of the Syllable OS kernel. The following features were developed and demonstrated:

- **Threading Demo**: A monolithic kernel-style threading system was implemented using a `Kernel` class that manages thread creation, execution, and synchronization using lock mechanisms.

- **Disk Partitioning**: A device manager module was simulated to handle disk geometry and partitioning logic, including registration, renaming, deletion, and visualization of device nodes.

- **File Operations**: A hierarchical file system was simulated, supporting file creation, reading, writing, and directory navigation, mimicking the Linux-based file structure of Syllable OS.

- **Memory Allocation**: We implemented First Fit and Best Fit contiguous memory allocation strategies to simulate basic memory management at the kernel level.

- **Synchronization Tree**: A semaphore-based synchronization system and resource tree were designed to manage concurrent access to shared resources between simulated processes.

- **Page Replacement**: The LRU (Least Recently Used) and Optimal page replacement algorithms were simulated to compare memory management strategies and evaluate performance based on page fault minimization.

---



## ▶️ How to Run

Depending on implementation language:

```bash
# For C++
g++ -o syllable_simulator main.cpp
./syllable_simulator

# For Python
python3 syllable_simulator.py
```

> Ensure you are using a terminal that supports standard input/output.

---

## 📄 License

This project is created for educational purposes as part of a university curriculum. All simulations and outputs are original and intended for academic demonstration only.

---

## 🙌 Acknowledgements

* Syllable OS documentation and project site: [https://syllable.metaproject.frl/](https://syllable.metaproject.frl/)
* Linux and Unix internals literature
* Academic OS references and textbooks

---
