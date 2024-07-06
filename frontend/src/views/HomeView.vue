<template>
  <v-container>
    <FeedbackFormDialog />
  </v-container>
</template>

<script>
import FeedbackFormDialog from '../components/FeedbackFormDialog.vue';

export default {
  components: {
    FeedbackFormDialog,
  },
};
</script>

<style scoped>
.container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>