# Polyglot Environment Setup

## Quick Setup Commands

### 1. Update Your Existing f_sharp Environment
```powershell
# Update your existing f_sharp environment
conda env update -f environment.yml

# Activate your f_sharp environment
conda activate f_sharp

# Register Python kernel with Jupyter (using f_sharp env)
python -m ipykernel install --user --name=f_sharp --display-name "Python (f_sharp)" --force
```

### 2. Install .NET Interactive (for F# support)
```powershell
# Verify .NET SDK is installed
dotnet --version

# Install .NET Interactive tool globally
dotnet tool install -g Microsoft.dotnet-interactive

# Register .NET kernels with Jupyter
dotnet interactive jupyter install
```

### 3. VS Code Extensions Required
- **Polyglot Notebooks** (ms-dotnettools.dotnet-interactive-vscode)
- **Jupyter** (ms-toolsai.jupyter)

## Testing Your Setup

1. Open `notebooks/polyglot_test.dib`
2. **Important**: Select kernels when prompted in VS Code:
   - F# cells → `.NET Interactive F#` 
   - Python cells → `Python (f_sharp)`
3. **Do NOT add magic commands** - Let VS Code handle kernel selection
4. Execute both cells - should output identical mathematical results

## ⚠️ Common Mistakes to Avoid

- **Don't add `#!fsharp` or `#!python` magic commands** - These interfere with proper kernel selection
- **Don't modify the `#!about` cell** - This provides kernel information
- **Select the correct kernel** in VS Code's kernel picker for each cell type

## Troubleshooting

### F# Kernel Not Available
```powershell
# Reinstall .NET Interactive
dotnet tool uninstall -g Microsoft.dotnet-interactive
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install
```

### Python Kernel Issues
```powershell
# Recreate kernel registration for f_sharp environment
conda activate f_sharp
python -m ipykernel install --user --name=f_sharp --display-name "Python (f_sharp)" --force
```

### Duplicate Output Issues
If you see duplicate outputs (e.g., "square(7) = 49 49" instead of "square(7) = 49"):

**This indicates corrupted kernel state. Follow these steps:**

```powershell
# 1. Restart .NET Interactive completely
dotnet tool uninstall -g Microsoft.dotnet-interactive
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install

# 2. Restart VS Code completely
# Close VS Code entirely, then reopen

# 3. Clear notebook outputs
# In VS Code: Command Palette → "Notebook: Clear All Outputs"

# 4. Run cells one by one
# Don't run multiple cells rapidly - let each complete first
```

**Prevention:** Never add `#!fsharp` or `#!python` magic commands manually!

### Environment Variables (if needed)
Add to your PATH:
- `%USERPROFILE%\.dotnet\tools` (for .NET tools)
- Your conda installation path

## Ready for Development!

Once both kernels work in `polyglot_test.dib`, you can:
- Create module-specific notebooks
- Use F# for symbolic/logical work
- Use Python for numerical analysis
- Combine both in the same notebook!
