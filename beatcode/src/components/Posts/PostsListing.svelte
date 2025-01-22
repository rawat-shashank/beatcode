<script lang="ts">
	import type { Post } from '$lib/types';
	import Pagination from './Pagination.svelte';
	import Search from './Search.svelte';
	import Table from './Table.svelte';

	export let postsListingData: Post[];
</script>

<div class="flex flex-col">
	<div class="-m-1.5 overflow-x-auto">
		<div class="inline-block min-w-full p-1.5 align-middle">
			<div
				class="divide-y divide-gray-200 rounded-lg border dark:divide-neutral-700 dark:border-neutral-700"
			>
				<!-- <div class="px-4 py-3">
					<Search />
				</div> -->
				<div class="overflow-hidden">
					<Table rows={postsListingData} />
				</div>
				<!-- <div class="px-4 py-1">
					<Pagination />
				</div> -->
			</div>
		</div>
	</div>
</div>
