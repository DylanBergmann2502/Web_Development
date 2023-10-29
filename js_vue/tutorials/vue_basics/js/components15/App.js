import Assignments from "./Assignments.js";
import Panel from "./Panel.js";

export default {
    components: { Assignments, Panel },

    template: `
        <div class="grid gap-6">
            <assignments></assignments>

            <panel>
                This is my default content.
            </panel>

            <panel>
                This is my default content.

                <template v-slot:heading>
                    This is my heading content.
                </template>
            </panel>

            <panel>
                This is my default content.

                <template v-slot:heading>
                    This is my heading content.
                </template>

                <template v-slot:footer>
                    Click here to learn more.
                </template>
            </panel>

            <panel theme="light">
                This is my default content.

                <template v-slot:heading>
                    This is my heading content.
                </template>

                <template v-slot:footer>
                    Click here to learn more.
                </template>
            </panel>
        </div>

    `,
}
