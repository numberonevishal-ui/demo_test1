def add_numbers(num1, num2):
    return sum(int(digit) for digit in str(num1 + num2))


def generate_claude_info_html():
    """Build an HTML page containing information about Claude."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Claude</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f3ee;
            color: #2b2b2b;
            line-height: 1.6;
        }
        header {
            background: linear-gradient(135deg, #d97757, #b8552f);
            color: #fff;
            padding: 48px 24px;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        header p {
            margin: 8px 0 0;
            font-size: 1.1rem;
            opacity: 0.95;
        }
        main {
            max-width: 800px;
            margin: 0 auto;
            padding: 32px 24px;
        }
        section {
            background: #fff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }
        section h2 {
            margin-top: 0;
            color: #b8552f;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        footer {
            text-align: center;
            padding: 24px;
            font-size: 0.9rem;
            color: #777;
        }
    </style>
</head>
<body>
    <header>
        <h1>Claude</h1>
        <p>An AI assistant built by Anthropic</p>
    </header>
    <main>
        <section>
            <h2>What is Claude?</h2>
            <p>
                Claude is a family of large language models created by Anthropic.
                It is designed to be helpful, honest, and harmless, and can assist
                with writing, analysis, coding, research, and everyday questions.
            </p>
        </section>
        <section>
            <h2>Key Capabilities</h2>
            <ul>
                <li>Natural conversation and question answering</li>
                <li>Writing and editing across many styles and formats</li>
                <li>Reading and reasoning over long documents</li>
                <li>Software engineering and code generation</li>
                <li>Summarization, translation, and data analysis</li>
            </ul>
        </section>
        <section>
            <h2>Model Family</h2>
            <ul>
                <li><strong>Claude Opus</strong> &mdash; the most capable model for complex tasks</li>
                <li><strong>Claude Sonnet</strong> &mdash; a balance of intelligence and speed</li>
                <li><strong>Claude Haiku</strong> &mdash; the fastest, most lightweight model</li>
            </ul>
        </section>
        <section>
            <h2>Built by Anthropic</h2>
            <p>
                Anthropic is an AI safety company focused on building reliable,
                interpretable, and steerable AI systems. Claude reflects this mission
                through a strong emphasis on safety and helpfulness.
            </p>
        </section>
    </main>
    <footer>
        <p>Generated page &mdash; information about Claude by Anthropic.</p>
    </footer>
</body>
</html>
"""
    return html


def write_claude_info_html(filename="claude_info.html"):
    """Write the Claude information HTML page to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_claude_info_html())
    return filename


num1 = 10
num2 = 20
print(add_numbers(num1, num2))

output_file = write_claude_info_html()
print(f"Claude information HTML page written to {output_file}")