# Home Theater Facade — Reference Implementation

Canonical teaching example for **Facade**.

- **Client:** `HomeTheaterClient`
- **Facade:** `HomeTheaterFacade`
- **Subsystem:** Amplifier, Projector, TheaterLights, StreamingPlayer

The Facade owns the common coordination protocol while subsystem objects retain their own responsibilities. Direct subsystem access remains possible.

This is a public teaching reference, not an answer key for the assessed transfer activity.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
