import os

from rich.console import Console
from rich.panel import Panel

if __name__ == "__main__":
    print(os.system("whoami"))
    print(os.environ.get("TERMINAL"))
    console = Console()
    console.print(
        Panel.fit(
            "[bold green]🤖 Voice-Enabled AI Agent[/bold green]\n"
            "[dim]Orchestrator-first · GPT-4o · Playwright · Wikipedia · Gmail[/dim]",
            border_style="green",
        )
    )
