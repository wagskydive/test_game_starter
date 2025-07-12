# Story Anchors

The `EventSystem` manages a list of `StoryAnchor` objects. Call `tick()` to
check for conditions and trigger anchors. Each anchor may define an `on_trigger`
callback that receives the anchor when it activates.
