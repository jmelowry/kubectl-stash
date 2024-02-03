import os
import json
from kubernetes import config, client

class KubectlStash:
    def __init__(self, namespace=None, context=None, environment=None):
        self.namespace = namespace
        self.context = context
        self.environment = environment
        self.kube_config_path = os.path.join(os.path.expanduser('~'), '.kube', 'config')

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

    def interactive_mode(self):
        """Interactively prompt the user to select a Kubernetes context, namespace, and environment."""
        contexts = self.list_contexts()
        if contexts:
            print("Available Kubernetes Contexts:")
            for index, context in enumerate(contexts):
                print(f"{index + 1}. {context['name']}")
            selected = int(input("Select a context by number: ")) - 1
            self.context = contexts[selected]['name']

        # Prompt for namespace if not provided
        if not self.namespace:
            self.namespace = input("Enter Kubernetes namespace: ")

        # Prompt for environment if not provided
        if not self.environment:
            self.environment = input("Enter environment: ")

        # Here, you can add logic to "stash" these selections or perform other actions.

    def run(self):
        """The main method to run the tool based on the provided or selected parameters."""
        if self.context:
            # Perform the actions needed based on the context, namespace, and environment
            print(f"Using context: {self.context}, namespace: {self.namespace}, environment: {self.environment}")
        else:
            print("No context selected.")

# Example usage within the same file (for testing purposes):
if __name__ == "__main__":
    ks = KubectlStash()
    ks.interactive_mode()
