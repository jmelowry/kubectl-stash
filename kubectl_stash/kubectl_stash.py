import os
import json
from kubernetes import config, client

class KubectlStash:
    def __init__(self, namespace=None, context=None, environment=None):
        self.namespace = namespace
        self.context = context
        self.environment = environment
        self.config_path = os.path.join(os.path.expanduser('~'), '.kubectl_stash')
        self.kube_config_path = os.path.join(os.path.expanduser('~'), '.kube', 'config')
        self.load_config()

    def load_kube_config(self):
        """Load Kubernetes configuration from the default location."""
        config.load_kube_config(config_file=self.kube_config_path)

    def list_contexts(self):
        """List all available Kubernetes contexts."""
        self.load_kube_config()
        contexts, active_context = config.list_kube_config_contexts()
        if not contexts:
            print("No contexts found in kubeconfig.")
        else:
            return contexts

    def load_config(self):
        """Load KubectlStash configuration."""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                config = json.load(file)
                self.namespace = config.get('namespace', self.namespace)
                self.context = config.get('context', self.context)
                self.environment = config.get('environment', self.environment)

    def save_config(self):
        """Save the current configuration to a file."""
        config = {
            'namespace': self.namespace,
            'context': self.context,
            'environment': self.environment
        }
        with open(self.config_path, 'w') as file:
            json.dump(config, file)

    def prompt_with_default(self, message, default=None):
        """Prompt the user with a default value."""
        userInput = input(f"{message} [{'<none>' if default is None else default}]: ").strip()
        return userInput or default

    def interactive_mode(self):
        """Interactively prompt the user to select a Kubernetes context, namespace, and environment."""
        try:
            contexts = self.list_contexts()
            if contexts:
                print("Available Kubernetes Contexts:")
                for index, context in enumerate(contexts):
                    print(f"{index + 1}. {context['name']}")
                selected = int(self.prompt_with_default("Select a context by number", 1 if self.context is None else [c['name'] for c in contexts].index(self.context) + 1)) - 1
                self.context = contexts[selected]['name']

            self.namespace = self.prompt_with_default("Enter Kubernetes namespace", self.namespace)
            self.environment = self.prompt_with_default("Enter environment", self.environment)

            self.save_config()

            print(f"Using context: {self.context}, namespace: {self.namespace}, environment: {self.environment}")
        except KeyboardInterrupt:
            print("\nExiting..")
        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        """The main method to run the tool based on the provided or selected parameters."""
        if self.context:
            # Perform the actions needed based on the context, namespace, and environment
            print(f"Using context: {self.context}, namespace: {self.namespace}, environment: {self.environment}")
        else:
            self.interactive_mode()

# Example usage within the same file (for testing purposes):
if __name__ == "__main__":
    ks = KubectlStash()
    ks.run()
