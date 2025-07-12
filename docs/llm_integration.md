# LLM Storytelling Integration

`generate_dialogue(prompt)` returns a simple stubbed response unless the
`DISABLE_LLM` environment variable is set to `1`.

Use `load_offline_model(path)` to enable an offline model. When loaded,
`generate_dialogue` will return responses prefixed with `[OFFLINE_LLM]`.
