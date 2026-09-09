#!/usr/bin/env bash
# Rollback to the pinned Ollama. `doas env` is required — plain VAR=x doas strips the
# environment and reinstalls latest, which is how this pin was lost once before.
ssh larry 'curl -fsSL https://ollama.com/install.sh -o /tmp/ollama-install.sh && \
  doas env OLLAMA_VERSION=0.31.1 sh /tmp/ollama-install.sh && \
  sleep 5 && ollama --version'
