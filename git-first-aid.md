# Git First Aid Guide

## 1. Undo the last commit (soft reset vs hard reset)

### Soft reset

Command:

```bash
git reset --soft HEAD~1
```

What happens:

- Last commit remove ho jata hai.
- Changes safe rehte hain.
- Files staged rehti hain.

Kab use karein:

Jab commit message galat ho ya commit dobara karna ho.

### Hard reset

Command:

```bash
git reset --hard HEAD~1
```

What happens:

- Last commit delete ho jata hai.
- Saare changes permanently remove ho jate hain.

Kab use karein:

Jab aapko commit aur changes dono hataane hon.

---

## 2. Remove a file committed by mistake

Command:

```bash
git rm secret.txt
git commit -m "Remove secret file"
```

What happens:

- File repository se remove ho jati hai.
- Naya commit create hota hai.

Kab use karein:

Jab galti se koi file commit ho jaye.

---

## 3. Recover work using git stash

Command:

```bash
git stash
```

Restore:

```bash
git stash pop
```

What happens:

- Temporary changes save ho jate hain.
- Baad mein restore kar sakte hain.

Kab use karein:

Jab branch switch karni ho.

---

## 4. Recover commits using git reflog

Command:

```bash
git reflog
```

Output:

```text
abc123 HEAD@{0}: commit: Add login feature
xyz456 HEAD@{1}: reset: moving to HEAD~1
```

Recover:

```bash
git reset --hard xyz456
```

What happens:

- Deleted commit wapas aa jata hai.

Kab use karein:

Jab galti se commit delete ho jaye.