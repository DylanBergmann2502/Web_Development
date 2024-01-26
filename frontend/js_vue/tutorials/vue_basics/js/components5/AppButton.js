export default {
    template: `
        <button
          :disabled="processing"
          class="bg-gray-200 hover:bg-gray-400 border rounded px-5 py-2 disabled:cursor-not-allowed"
        >
            <slot />
        </button>
    `,

    data() {
        return {
            processing: true,
        };
    }
}
