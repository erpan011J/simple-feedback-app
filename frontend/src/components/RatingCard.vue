<template>
    <div class="custom-rating">
      <div class="stars">
        <v-icon v-for="n in 5" :key="n" :class="{ 'filled': n <= internalRating }" @click="rate(n)">
          {{ n <= internalRating ? 'mdi-star' : 'mdi-star' }}
        </v-icon>
      </div>
      <div class="numbers">
        <span v-for="n in 5" :key="n" class="number" @click="rate(n)">
          {{ n }}
        </span>
      </div>
      <div class="labels">
        <span class="label">Very Dissatisfied</span>
        <span class="label">Very Satisfied</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      value: Number,
    },
    data() {
      return {
        internalRating: this.value || 0,
      };
    },
    watch: {
      value(newValue) {
        this.internalRating = newValue;
      },
    },
    methods: {
      rate(value) {
        this.internalRating = value;
        this.$emit('input', this.internalRating);
      },
    },
  };
  </script>
  
  <style scoped>
  .custom-rating {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .stars {
    display: flex;
  }
  
  .v-icon {
    font-size: 2.85rem !important;
    cursor: pointer !important;
    margin: 0 5px;
    color: #e0e0e0 !important;
  }
  
  .v-icon.filled {
    color: #757575 !important;
  }
  
  .numbers {
    display: flex;
    margin-top: 20px;
  }
  
  .number {
    font-weight: bold;
    font-size: 1rem;
    cursor: pointer;
    margin: 0 24px;
  }
  
  .labels {
    display: flex;
    justify-content: space-evenly;
    width: 100%;
    margin-top: 10px;
  }
  
  .label {
    font-size: 0.8rem;
    color: rgba(0, 0, 0, 0.6);
  }
  </style>
  