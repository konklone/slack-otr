## Slack OTR

Slack OTR is designed to allow a community to use a free Slack, while also destroying most or all of its message history after a certain point.

This tool will delete all messages and threads in public channels. It will show up as a bot that auto-joins all public channels.

### Setup

Slack OTR requires **Python 3.7** or higher. The author recommends using [`pyenv`](https://github.com/pyenv/pyenv) for Python version management.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run it:

```bash
./slack-otr
```

**NOTE:** For your safety, Slack OTR's code currently will, by default, only sweep a test channel named `#otr-bot-testing`.

To tell Slack OTR to sweep all channels, comment that line out and uncomment the line above that lists all public channels.

(This is obviously a hack, and will be improved with proper command line flags.)

## Attribution

Slack OTR is developed by [Eric Mill](https://twitter.com/konklone).

## Open source license and contributions

Slack OTR is open source, under the [BSD-3 license](LICENSE).

By contributing code to this open source project, you are agreeing to license your contributions under the same BSD-3 license.
