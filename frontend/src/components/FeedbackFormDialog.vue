<template>
  <v-dialog v-model="dialog" max-width="600" @keydown.esc="closeDialog" @click:outside="closeDialog"
    @close="closeDialog">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on">
        <v-icon left>mdi-comment-outline</v-icon> Give Feedback
      </v-btn>
    </template>
    <v-card>
      <v-card-text>
        <h2 class="feedback-title">How would you rate your satisfaction with our product?</h2>
        <RatingCard v-model="rating" />
        <v-textarea v-model="comment" label="Additional Comments" rows="3" outlined
          class="pt-8 feedback-text-area"></v-textarea>
      </v-card-text>
      <v-card-actions class="d-flex">
        <v-btn color="primary" @click="submitFeedback" :disabled="!rating" class="btn-submit">
          Submit
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-snackbar v-model="snackbar" :timeout="3000" color="error" top>
      {{ snackbarText }}
    </v-snackbar>
  </v-dialog>

</template>

<script>
import RatingCard from './RatingCard.vue';
import { submitFeedback } from '@/services/api';
import router from '@/router';

export default {
  components: {
    RatingCard,
  },
  data() {
    return {
      dialog: false,
      rating: 0,
      comment: '',
      snackbar: false,
      snackbarText: '',
    };
  },
  methods: {
    async submitFeedback() {
      try {
        const feedback = {
          score: this.rating,
          comment: this.comment,
        };
        await submitFeedback(feedback);
        this.closeDialog();
        router.push({ path: '/thankyou' });
      } catch (error) {
        if (error.response.status === 400) {
          this.snackbarText = error.response?.data?.detail || 'Please fix the validation errors before submitting.';
        } else if (error.response.status === 500) {
          this.snackbarText = 'An internal server error occurred. Please try again later.';
        } else {
          this.snackbarText = 'An error occurred while submitting feedback.';
        }
        this.snackbar = true;
      }
    },
    closeDialog() {
      this.dialog = false;
      this.rating = 0;
      this.comment = '';
    },
  },
};
</script>

<style scoped>
.v-card__text::v-deep {
  padding-top: 75px !important;
}

.subtitle-1 {
  padding-bottom: 10px;
  font-weight: bold !important;
  color: black;
}

.text-center {
  text-align: center;
}

.btn-submit {
  width: 80%;
  margin: 0 auto 20px auto;
}

.feedback-text-area {
  width: 82%;
  margin: 0 auto !important;
}

.feedback-title {
  font-size: 19px;
  color: black;
  text-align: left;
  margin: 0px 10px 36px 52px;
}
</style>
