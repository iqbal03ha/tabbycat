<template>

  <drag-and-drop-layout>

    <drag-and-drop-actions slot="actions" prioritise="true" allocate="true" shard="true"
                           @shard="shard" @allocate="allocate" @prioritise="prioritise">
      <template slot="default-highlights">
        <button class="btn btn-outline-secondary disabled" v-text="gettext('Key')"></button>
        <button class="btn conflictable conflicts-toolbar hover-histories-2-ago"
                data-toggle="tooltip" v-text="gettext('Seen')"
                :title="('Has judged this team or with this adjudicator previously')"></button>
        <button class="btn conflictable conflicts-toolbar hover-institution"
                data-toggle="tooltip" v-text="gettext('Institution')"
                :title="('Is from the same institution as this team or panelist.')"></button>
        <button class="btn conflictable conflicts-toolbar hover-adjudicator"
                data-toggle="tooltip" v-text="gettext('Conflict')"
                :title="('Has a nominated conflict with this team or panelist.')"></button>
        <button class="btn panel-incomplete"
                data-toggle="tooltip" v-text="gettext('Incomplete')"
                :title="('Panel is missing a chair or enough adjudicators for a voting majority.')"></button>
      </template>
    </drag-and-drop-actions>

    <template slot="debates">
      <drag-and-drop-debate v-for="debate in debatesOrPanels" :key="debate.id" :debateOrPanel="debate">
        <debate-importance slot="importance" :debateOrPanel="debate"></debate-importance>
        <template slot="adjudicators">fancy adjs UI</template>
        <template slot="venue"><span></span></template><!--Hide Venues-->
      </drag-and-drop-debate>
    </template>

    <template slot="modals">
      <modal-for-sharding :intro-text="gettext(intro)"></modal-for-sharding>
      <modal-for-allocating :intro-text="gettext(allocateIntro)"
                            :context-of-action="'allocate_debate_adjs'"></modal-for-allocating>
      <modal-for-prioritising :intro-text="gettext(prioritiseIntro)"
                              :context-of-action="'prioritise_debate_adjs'"></modal-for-prioritising>
    </template>

  </drag-and-drop-layout>

</template>

<script>
import EditEitherAdjudicatorsSharedMixin from './EditEitherAdjudicatorsSharedMixin.vue'

export default {
  mixins: [EditEitherAdjudicatorsSharedMixin],
  data: () => ({
    intro: `Sharding narrows the panels displayed to show only a specific subset of all
      panels available.`,
    allocateIntro: `Using auto-allocate will remove adjudicators from all debates and create a new
      allocations in their place.`,
    prioritiseIntro: `Using auto-prioritise will remove all existing debate priorities and assign
      new ones.`,
  }),
}
</script>