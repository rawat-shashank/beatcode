<script lang="ts">
	import { base } from '$app/paths';
	import type { Post } from '$lib/types';

	export let rows: Post[];
</script>

<table class="min-w-full divide-y divide-gray-200 dark:divide-neutral-700">
	<thead class="bg-gray-50 dark:bg-neutral-700">
		<tr>
			<th scope="col" class="px-4 py-3 pe-0">
				<div class="flex h-5 items-center">
					<input
						id="hs-table-pagination-checkbox-all"
						type="checkbox"
						class="rounded border-gray-200 text-blue-600 focus:ring-blue-500 dark:border-neutral-500 dark:bg-neutral-700 dark:checked:border-blue-500 dark:checked:bg-blue-500 dark:focus:ring-offset-gray-800"
					/>
					<label for="hs-table-pagination-checkbox-all" class="sr-only">Checkbox</label>
				</div>
			</th>
			<th
				scope="col"
				class="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
				>Title</th
			>
			<th
				scope="col"
				class="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
				>Description</th
			>
			<th
				scope="col"
				class="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
				>Difficulty</th
			>
			<th
				scope="col"
				class="px-6 py-3 text-end text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
				>Action</th
			>
		</tr>
	</thead>
	<tbody class="divide-y divide-gray-200 dark:divide-neutral-700">
		{#each rows as row}
			<tr>
				<td class="py-3 ps-4">
					<div class="flex h-5 items-center">
						<input
							id="hs-table-pagination-checkbox-1"
							type="checkbox"
							class="rounded border-gray-200 text-blue-600 focus:ring-blue-500 dark:border-neutral-700 dark:bg-neutral-800 dark:checked:border-blue-500 dark:checked:bg-blue-500 dark:focus:ring-offset-gray-800"
						/>
						<label for="hs-table-pagination-checkbox-1" class="sr-only">Checkbox</label>
					</div>
				</td>
				<td
					class="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-800 dark:text-neutral-200"
					>{row.title}</td
				>
				<td class="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200"
					>{row.description.slice(0, 40)}...</td
				>
				<td class="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200"
					>{row.difficulty}</td
				>
				<td class="whitespace-nowrap px-6 py-4 text-end text-sm font-medium">
					<a href="{base}/posts/{row.id}/edit">
						<button
							type="button"
							class="inline-flex items-center gap-x-2 rounded-lg border border-transparent text-sm font-semibold text-blue-600 hover:text-blue-800 focus:text-blue-800 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:text-blue-500 dark:hover:text-blue-400 dark:focus:text-blue-400"
						>
							Edit
						</button>
					</a>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
