#!/bin/bash
# scripts/bootstrap-env.sh

echo "Initializing BAAS environment files..."

# Root env
if [ ! -f .env.development ]; then
    cp .env.development.example .env.development
    echo "Created .env.development"
fi

# API env
if [ ! -f apps/api/.env.development.local ]; then
    cp apps/api/.env.development.example apps/api/.env.development.local
    echo "Created apps/api/.env.development.local"
fi

# Web env
if [ ! -f apps/web/.env.local ]; then
    cp apps/web/.env.local.example apps/web/.env.local
    echo "Created apps/web/.env.local"
fi

# Worker env
if [ ! -f apps/worker/.env.development.local ]; then
    cp apps/worker/.env.development.example apps/worker/.env.development.local
    echo "Created apps/worker/.env.development.local"
fi

echo "Done. Please update the keys in the .local files."
