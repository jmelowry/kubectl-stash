#!/usr/bin/env python3

import argparse
from kubectl_stash.kubectl_stash import KubectlStash

def main():
    parser = argparse.ArgumentParser(description="kubectl-stash CLI tool")
    parser.add_argument("-n", "--namespace", help="Kubernetes namespace")
    parser.add_argument("-c", "--context", help="Kubernetes context name")
    parser.add_argument("-e", "--environment", help="Environment name")

    args = parser.parse_args()

    if not (args.namespace and args.context and args.environment):
        # Handle interactive input
        KubectlStash().interactive_mode()
    else:
        # Command line mode
        KubectlStash(namespace=args.namespace, context=args.context, environment=args.environment).run()

if __name__ == "__main__":
    main()
