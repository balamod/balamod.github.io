<h1>Frequently Asked Questions</h1>

<h2>What is balamod?</h2>

<p>
  Balamod is a mod loader and framework for the game <a href="https://store.steampowered.com/app/2379780/Balatro/">Balatro</a>.
  It allows users and modders to modify the game's code, mechanics and assets.
</p>

<h2>How do I install balamod?</h2>

<!-- <p>Head on to the <a href="/docs/user-guide/installation">installation guide</a> to learn how to install balamod.</p> -->

<h2>In what language are mods/Balatro written in?</h2>

<p>
  Balatro is written in <a href="https://www.lua.org/">Lua</a>, and so are the mods and APIs.

  <!-- Balatro is built using the <a href="https://love2d.org/">LÖVE</a> framework, which is also written in Lua. -->
</p>

<h2>Where are my mods/apis stored?</h2>

<p>
  Depending on your operating system, balamod stores mods and APIs in different locations.

  <!-- You can refer to <a href="https://love2d.org/wiki/love.filesystem">this page</a> to know where LÖVE stores files on your system. -->
</p>
<ul>
  <li>On Windows, the default location is <code>%appdata%\Balatro\mods</code>.</li>
  <li>On Linux, the default location is <code>~/.local/share/Balatro/mods</code>, or <code>$XDG_DATA_HOME/Balatro/mods</code> if the environment variable is set.</li>
  <li>On macOS, the default location is <code>~/Library/Application Support/Balatro/mods</code>.</li>
</ul>

<h2>How do I create a mod?</h2>

<p>
  <!-- Head on to the <a href="/docs/modding-guide/getting-started">modding guide</a> to learn how to create a mod. -->

  In short, you need to create a new lua file in the mods folder, and insert your mod in the <code>mods</code> table.
</p>

<h2>Help, on MacOS, Balatro crashes after installing balamod, and talks about "SSL"!</h2>

<p>
  No worries, this is a known issue. You can fix it by installing OpenSSL using Homebrew.<br/>
  <!-- Open a terminal, and run the following command, which installs <a href="https://brew.sh/">Homebrew</a> and OpenSSL 3.0: -->

</p>
<Code language="bash">/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install openssl@3</Code>

<h2>Is this compatible with <em>&lt;insert modloader of choice&gt;</em> </h2>

<p>
  Yes and no. Balamod is a mod loader, and as such, injects a lot of code into the game to make things just work.
  Installing other mod loaders may work, or may not, but in any case, no support will be provided for such configurations.

  In theory, you should not need any other mod loader, as balamod is designed to be as flexible and lightweight as possible,
  while providing all of the necessary tools for both modders and users.

  Other mod loaders include the also popular <em>Steammodded</em> loader, which is not compatible with balamod at this time.
</p>

<script lang="ts">
  import Code from '$lib/components/Code.svelte';
</script>
