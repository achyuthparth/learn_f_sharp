from pathlib import Path
import re

def parse_booklist(booklist_path):
    tag_to_anchor = {}
    with open(booklist_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        match = re.match(r"^-\s*\[#([A-Z]+)\]\s+\*(.+?)\*", line)
        if match:
            tag = match.group(1)
            title = match.group(2)  # Just the book title between asterisks
            # Create simple, clean GitHub anchor
            anchor = re.sub(r"[^\w\s]", "", title).strip().lower().replace(" ", "-")
            tag_to_anchor[tag] = anchor
    return tag_to_anchor

def autolink_references(references_path, booklist_path):
    tag_to_anchor = parse_booklist(booklist_path)

    with open(references_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Prevent double-linking by skipping already-linked tags
    def link_tag(match):
        tag = match.group(1)
        
        # Check if this tag is in our booklist and not already linked
        if tag in tag_to_anchor:
            # Look for existing links with this tag
            existing_link_pattern = rf"\[#{re.escape(tag)}\]\([^)]*\)"
            if not re.search(existing_link_pattern, content):
                anchor = tag_to_anchor[tag]
                return f"[#{tag}](../../docs/booklist.md#{anchor})"
        
        return match.group(0)

    # Find bare [#TAG] patterns that aren't already part of links
    # Use negative lookahead to avoid matching [#TAG]( patterns
    updated_content = re.sub(r"\[#([A-Z]+)\](?!\()", link_tag, content)

    with open(references_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Linked references in: {references_path}")

def bulk_autolink_all_references(repo_root: Path, booklist_path: Path):
    print("🔍 Scanning for references to link...")

    reference_files = list(repo_root.rglob("*_references.md"))
    if not reference_files:
        print("⚠️ No *_references.md files found.")
        return

    for ref_path in reference_files:
        try:
            autolink_references(ref_path, booklist_path)
        except Exception as e:
            print(f"❌ Failed to process {ref_path} — {e}")

if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]  # /docs/utilities/

    booklist_path = repo_root / "docs" / "booklist.md"

    # Single file mode
    autolink_references(
        references_path=repo_root / "part1-functional-programming" / "modules" / "01-logic-and-proofs" / "1_1_references.md",
        booklist_path=booklist_path
    )

    # Or enable this for bulk mode
    # bulk_autolink_all_references(repo_root, booklist_path)
