<template>
  <v-container fluid>
    <v-row justify="center" align="center" style="height: 100vh;">
      <v-col cols="12" md="8">
        <v-card class="pa-8" outlined>
          <v-icon size="100" class="green--text">mdi-check-circle-outline</v-icon>
          <h1 class="headline text-center">Thank You!</h1>
          <p class="subheading text-center">Your feedback has been submitted successfully.</p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'ThankYouView',
}
</script>

<style scoped>
.headline {
  margin-top: 20px;
  margin-bottom: 10px;
}

.subheading {
  margin-bottom: 20px;
}
</style>
