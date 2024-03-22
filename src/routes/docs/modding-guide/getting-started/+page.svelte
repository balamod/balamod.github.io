<h1>Getting Started</h1>

<h2>Creating a mod</h2>

<p>
  A balamod mod is a single lua file which adds whatever you want to the game. When balamod is installed, it
  injects itself in the love2d game hooks, so that mods can edit game function, run code before and after the game
  renders frames and so on
</p>

<h2>Hooks provided</h2>

<ul>
  <li><a href="#on_game_load"><pre>on_game_load</pre></a></li>
  <li><a href="#on_game_quit"><pre>on_game_quit</pre></a></li>
  <li><a href="#on_pre_update"><pre>on_pre_update</pre></a></li>
  <li><a href="#on_post_update"><pre>on_post_update</pre></a></li>
  <li><a href="#on_enable"><pre>on_enable</pre></a></li>
  <li><a href="#on_disable"><pre>on_disable</pre></a></li>
  <li><a href="#menu"><pre>menu</pre></a></li>
  <li><a href="#on_pre_render"><pre>on_pre_render</pre></a></li>
  <li><a href="#on_post_render"><pre>on_post_render</pre></a></li>
  <li><a href="#on_key_pressed"><pre>on_key_pressed</pre></a></li>
  <li><a href="#on_key_released"><pre>on_key_released</pre></a></li>
  <li><a href="#on_mouse_pressed"><pre>on_mouse_pressed</pre></a></li>
  <li><a href="#on_mouse_released"><pre>on_mouse_released</pre></a></li>
  <li><a href="#on_error"><pre>on_error</pre></a></li>
  <li><a href="#on_mousewheel"><pre>on_mousewheel</pre></a></li>
</ul>

<h3 id="on_game_load">On game load</h3>

<p>
  This hook is called when the game is loaded. This is the first hook that is called, and is called only once.
  This hooks gets one argument, which is the command line arguments passed into the game, as a LUA table.<br>
  Arguments are passed in order, and are separated by spaces. Each argument will be a separate entry in the table.
</p>

<h3 id="on_game_quit">On game quit</h3>

<p>
  This hook is called when the game is quit. This is the last hook that is called, and is called only once.
  This hooks gets no arguments.
</p>

<h3 id="on_pre_update">On pre update</h3>

<p>
  This hook is called before the game updates. This is called every frame, before the game updates.
  This hooks gets one argument, which is the time since the last frame, in seconds.
</p>

<h3 id="on_post_update">On post update</h3>

<p>
  This hook is called after the game updates. This is called every frame, after the game updates.
  This hooks gets one argument, which is the time since the last frame, in seconds.
</p>

<h3 id="on_enable">On enable</h3>

<p>
  This hook is called when the mod is enabled. This is called every time the mod is enabled.
  This hooks gets no arguments.<br />

  For all intents and purposes, this hook is to be used to initialize your mod's variables.
</p>


<h3 id="on_disable">On disable</h3>

<p>
  This hook is called when the mod is disabled. This is called every time the mod is disabled.
  This hooks gets no arguments.<br />

  For all intents and purposes, this hook is to be used to clean up your mod's variables.
</p>


<h3 id="menu">Menu</h3>

<p>
  This hook should return a menu render (using the game's UI toolkit) to be displayed
  in the mod loader menu. You can use this hook to add buttons, sliders, textboxes, and so on.

  This hook gets no arguments.

  The menu can be (and should be) used to display configuration options for your mod.
</p>

<h3 id="on_pre_render">On pre render</h3>

<p>
  This hook is called before the game renders. This is called every frame, before the game renders.
  This hooks gets no arguments.

  This is called once per frame, in the love.draw function.
</p>

<h3 id="on_post_render">On post render</h3>

<p>
  This hook is called after the game renders. This is called every frame, after the game renders.
  This hooks gets no arguments.

  This is called once per frame, in the love.draw function.
</p>

<h3 id="on_key_pressed">On key pressed</h3>

<p>
  This hook is called when a key is pressed. This is called every time a key is pressed.
  This hooks gets one argument, which is the key that was pressed.

  You can return a boolean value from this hook to prevent the game from processing the key press.

  Returning true will cancel the game event handling, return false (or nil) otherwise.
</p>


<h3 id="on_key_released">On key released</h3>

<p>
  This hook is called when a key is released. This is called every time a key is released.
  This hooks gets one argument, which is the key that was released.

  You can return a boolean value from this hook to prevent the game from processing the key release.

  Returning true will cancel the game event handling, return false (or nil) otherwise.
</p>


<h3 id="on_mouse_pressed">On mouse pressed</h3>

<p>
  This hook is called when a mouse button is pressed. This is called every time a mouse button is pressed.
  This hooks gets the x, y coordinates of the mouse, the button that was pressed and the number of touches (in case of touch screens).

  You can return a boolean value from this hook to prevent the game from processing the mouse button press.

  Returning true will cancel the game event handling, return false (or nil) otherwise.
</p>


<h3 id="on_mouse_released">On mouse released</h3>

<p>
  This hook is called when a mouse button is released. This is called every time a mouse button is released.
  This hooks gets the x, y coordinates of the mouse and the button that was released.

  You can return a boolean value from this hook to prevent the game from processing the mouse button release.

  Returning true will cancel the game event handling, return false (or nil) otherwise.
</p>

<h3 id="on_error">On error</h3>

<p>
  This hook is called when an error occurs. This is called every time an error occurs, before the game crashes.

  This hooks gets one argument, which is the error message.
</p>

<h3 id="on_mousewheel">On mousewheel</h3>

<p>
  This hook is called when the mouse wheel is scrolled. This is called every time the mouse wheel is scrolled.
  This hooks gets the x, y coordinates of the mouse.

  You can return a boolean value from this hook to prevent the game from processing the mouse wheel scroll.

  Returning true will cancel the game event handling, return false (or nil) otherwise.
</p>
