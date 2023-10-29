export default {
    template: `
        <button
          :disabled="processing"
          :class="{
            'border rounded px-5 py-2 disabled:cursor-not-allowed': true,

            'bg-blue-600 hover:bg-blue-700': type === 'primary',
            'bg-green-200 hover:bg-green-400': type === 'secondary',
            'bg-gray-200 hover:bg-gray-400': type === 'muted',

            'is-loading': processing,
          }"
        >
            <slot />
        </button>
    `,

    props: {
        // This is the name of the prop
        type: {
            // This is the type of the prop
            type: String,
            default: "primary"
        },

        processing: {
            type: Boolean,
            default: false
        }
    },
}
