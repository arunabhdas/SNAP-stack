<script lang='ts'>
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	import { AppBar, AppRail, AppShell } from '@skeletonlabs/skeleton';
</script>

<AppShell>
	<AppBar>
		<h3 class="text-left">SNAP Stack</h3>
	</AppBar>
		<slot />
</AppShell>
