#!/usr/bin/env bash
# Serialize Git-mutating Vault automation without locking ordinary Obsidian reads.
set -euo pipefail

# GitHub calculates commit contributions using the timezone embedded in the
# author timestamp. The Vault's daily boundary is Korea Standard Time.
export TZ=Asia/Seoul

repo=$(git rev-parse --show-toplevel)
cd "$repo"
exec 9>"$repo/.git/hermes-vault-sync.lock"
if ! flock -n 9; then
  printf '보류: 다른 Vault 동기화 작업이 Git 잠금을 보유하고 있습니다.\n' >&2
  exit 75
fi
exec "$@"
