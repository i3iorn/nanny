<template>
  <section>
    <h1>Tasks</h1>
    <!-- TODO: Display tasks and integrate with backend -->
    <button @click="fetchTasks">Load Tasks</button>
    <ul>
      <li v-for="task in tasks" :key="task.id">{{ task.title }}</li>
    </ul>
  </section>
</template>

<script>
import { getTasks } from '../services/apiClient.js'

export default {
  name: 'TaskList',
  data() {
    return {
      tasks: []
    }
  },
  methods: {
    async fetchTasks() {
      this.tasks = await getTasks()
    }
  }
}
</script>
