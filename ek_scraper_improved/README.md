# ek-scraper (Improved v2)

Verbesserte Version des ek-scrapers für kleinanzeigen.de mit besseren Anti-Blocking-Maßnahmen, robusterem Parsing, erweiterten Filtern und mehr Benachrichtigungskanälen.

## Wichtige Verbesserungen gegenüber Original

- **Rate Limiting & Delays**: Zufällige Verzögerungen + sequentielles Laden statt massiv parallel
- **Robusteres Scraping**: Bessere Fehlerbehandlung, Timeouts, Retries mit Backoff
- **Erweiterte Filter**: Zusätzlich Preis-Min/Max Filter
- **Bessere Secrets-Handhabung**: Unterstützung für `.env` Dateien via `pydantic-settings`
- **Zusätzliche Notifications**: Telegram Bot (neben Pushover & ntfy.sh)
- **Besseres Logging**: Console + Rotating File Logger
- **Robusteres HTML-Parsing**: Mehrere Selektoren + klare Fehlermeldungen bei Änderungen
- **Bessere CLI**: Verbesserte Hilfe und Beispiele

## Installation (Development)

```bash
cd ek-scraper-improved
uv sync
```

Oder als Tool:

```bash
uv tool install -e .
```

## Usage

Siehe Original README für Grundlagen. Die neue Version unterstützt zusätzlich:

```json
{
  "filter": {
    "exclude_topads": true,
    "exclude_patterns": ["regex hier"],
    "price_min": 300,
    "price_max": 1200
  },
  "notifications": {
    "telegram": {
      "bot_token": "...",
      "chat_id": "..."
    }
  }
}
```

## Empfohlene Cronjob Frequenz

**Nicht öfter als alle 15–30 Minuten** laufen lassen, um nicht geblockt zu werden.

```cron
*/20 * * * * /path/to/ek-scraper run /path/to/config.json >> /var/log/ek-scraper.log 2>&1
```

## Bekannte Limitationen (auch in v2)

- Scraping von kleinanzeigen.de verstößt potenziell gegen die AGB. Nutzung auf eigenes Risiko.
- Bei starken Layout-Änderungen auf der Seite muss das Parsing ggf. angepasst werden.