# learn_f_sharp
Learning Functional Programming via F# with Polyglot Notebooks

## 🚀 Quick Start

### 1. Environment Setup
```powershell
# Update your existing f_sharp environment
conda env update -f environment.yml
conda activate f_sharp

# Register Python kernel
python -m ipykernel install --user --name=f_sharp --display-name "Python (f_sharp)" --force

# Install .NET Interactive for F#
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install
```

### 2. Test Your Setup
Open `notebooks/polyglot_test.dib` in VS Code and run both F# and Python cells.

### 3. Start Learning
- **Part 1**: Functional Programming fundamentals
- **Part 2**: Linear Algebra with F# + Python
- **Part 3**: Calculus & Numerical Methods
- **Part 4**: Mathematical Analysis

## 📁 Project Structure

- `environment.yml` - Conda environment specification
- `POLYGLOT_SETUP.md` - Detailed setup instructions
- `notebooks/` - Interactive learning notebooks (.dib format)
- `part1-functional-programming/` - Core F# concepts
- `part2-linear-algebra/` - Matrix operations & visualization
- `part3-calculus-numerics/` - Numerical methods
- `part4-analysis/` - Advanced mathematical analysis

## 🛠️ Prerequisites

- **VS Code** with Polyglot Notebooks extension
- **.NET SDK** (7.0 or later)
- **Anaconda/Miniconda**
- **Git** for version control

Ready to dive into functional programming? Start with the setup guide!
