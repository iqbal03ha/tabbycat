<script>
// Note parent component can pass the handledrop function; i.e. @handledrop="handledrop"
// Note the kebab case — is required by vue

export default {
  props: {
    locked: false,
    handleDrop: Function,
    dropContext: Object, // Passed to the handler of the item
  },
  data: function () {
    return {
      dragCounter: 0,
      aboutToDrop: false,
    }
  },
  computed: {
    droppableClasses: function () {
      let classes = 'vue-droppable '
      if (this.locked) {
        classes += ' vue-droppable-locked'
      } else if (this.aboutToDrop) {
        classes += ' vue-droppable-enter'
      }
      return classes
    },
  },
  methods: {
    dragEnter: function (event) {
      this.dragCounter += 1
      this.aboutToDrop = true
    },
    dragLeave: function (event) {
      this.dragCounter -= 1
      if (this.dragCounter === 0) {
        this.aboutToDrop = false
      }
    },
    drop: function (event) {
      // Firefox needs to prevent original actions
      if (event.preventDefault) { event.preventDefault() }
      if (event.stopPropagation) { event.stopPropagation() }
      this.dragCounter = 0
      if (this.locked) {
        return // Don't allow
      }
      this.aboutToDrop = false
      // Send data to parent's handler method (after deserialising it)
      const dragPayload = JSON.parse(event.dataTransfer.getData('text'))
      this['handleDrop'](dragPayload, this.dropContext) // Call page-specific method handler passed down
    },
  },
}
</script>
}
