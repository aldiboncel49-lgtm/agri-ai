#!/usr/bin/env python3
"""
🌾 AgriAI CLI - Asisten Pertanian Cerdas
Powered by Claude AI (Anthropic)
"""

import os
import sys
from anthropic import Anthropic
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.text import Text
from dotenv import load_dotenv

load_dotenv()

console = Console()

SYSTEM_PROMPT = """Kamu adalah AgriAI, asisten pertanian yang cerdas dan berpengalaman. 
Kamu memiliki keahlian mendalam tentang:
- Teknik budidaya tanaman pangan, hortikultura, dan perkebunan
- Pengendalian hama dan penyakit tanaman
- Manajemen irigasi dan kebutuhan air tanaman
- Pemupukan dan kesuburan tanah
- Pertanian organik dan berkelanjutan
- Cuaca dan iklim yang mempengaruhi pertanian
- Pasca panen dan pengolahan hasil pertanian
- Ekonomi pertanian dan pemasaran hasil tani

Berikan jawaban yang praktis, mudah dipahami petani, dan berbasis ilmu pertanian yang benar.
Gunakan bahasa Indonesia yang santai namun informatif.
Jika ada pertanyaan di luar pertanian, arahkan kembali ke topik pertanian."""

WELCOME_TEXT = """
╔══════════════════════════════════════════╗
║         🌾  AgriAI CLI  🌾              ║
║   Asisten Pertanian Cerdas Indonesia    ║
╚══════════════════════════════════════════╝

Tanya apa saja seputar pertanian!
Ketik 'exit' atau 'keluar' untuk keluar.
Ketik 'baru' untuk memulai percakapan baru.
"""


def get_api_key():
    """Ambil API key dari environment variable."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print(
            "[bold red]❌ Error:[/bold red] ANTHROPIC_API_KEY tidak ditemukan!\n"
            "Silakan set environment variable:\n"
            "  [cyan]export ANTHROPIC_API_KEY='your-api-key-here'[/cyan]\n"
            "atau buat file [cyan].env[/cyan] dan isi:\n"
            "  [cyan]ANTHROPIC_API_KEY=your-api-key-here[/cyan]"
        )
        sys.exit(1)
    return api_key


def print_welcome():
    """Tampilkan pesan sambutan."""
    console.print(WELCOME_TEXT, style="bold green")


def chat(client: Anthropic, conversation_history: list, user_input: str) -> str:
    """Kirim pesan ke Claude dan dapatkan respons."""
    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=conversation_history,
    )

    assistant_message = response.content[0].text
    conversation_history.append(
        {"role": "assistant", "content": assistant_message}
    )

    return assistant_message


def main():
    """Fungsi utama CLI."""
    api_key = get_api_key()
    client = Anthropic(api_key=api_key)

    print_welcome()

    conversation_history = []
    session_count = 1

    console.print(
        f"[dim]📋 Sesi #{session_count} dimulai[/dim]\n"
    )

    while True:
        try:
            user_input = Prompt.ask("\n[bold green]🧑‍🌾 Kamu[/bold green]").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "keluar", "quit", "q"]:
                console.print(
                    "\n[bold yellow]👋 Terima kasih telah menggunakan AgriAI! Selamat bertani! 🌾[/bold yellow]\n"
                )
                break

            if user_input.lower() in ["baru", "new", "reset"]:
                conversation_history = []
                session_count += 1
                console.print(
                    f"\n[dim]🔄 Sesi #{session_count} dimulai - percakapan direset[/dim]\n"
                )
                continue

            if user_input.lower() in ["bantuan", "help", "?"]:
                console.print(
                    Panel(
                        "[cyan]Perintah tersedia:[/cyan]\n"
                        "  • [bold]baru[/bold] / new    - Reset percakapan\n"
                        "  • [bold]bantuan[/bold] / help - Tampilkan bantuan\n"
                        "  • [bold]keluar[/bold] / exit  - Keluar dari program\n\n"
                        "[cyan]Contoh pertanyaan:[/cyan]\n"
                        "  • Bagaimana cara menanam padi yang baik?\n"
                        "  • Tanaman cabai saya daunnya menguning, kenapa?\n"
                        "  • Berapa dosis pupuk urea untuk jagung 1 hektar?\n"
                        "  • Cara membuat pupuk kompos dari limbah pertanian",
                        title="💡 Bantuan",
                        border_style="cyan",
                    )
                )
                continue

            # Tampilkan spinner saat menunggu respons
            with console.status("[bold yellow]🌱 AgriAI sedang berpikir...[/bold yellow]"):
                response = chat(client, conversation_history, user_input)

            # Tampilkan respons dalam panel yang menarik
            console.print(
                Panel(
                    Markdown(response),
                    title="[bold green]🌾 AgriAI[/bold green]",
                    border_style="green",
                    padding=(1, 2),
                )
            )

        except KeyboardInterrupt:
            console.print(
                "\n\n[bold yellow]👋 Program dihentikan. Selamat bertani! 🌾[/bold yellow]\n"
            )
            break
        except Exception as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}\n")
            console.print("[dim]Coba lagi atau ketik 'keluar' untuk keluar.[/dim]")


if __name__ == "__main__":
    main()
