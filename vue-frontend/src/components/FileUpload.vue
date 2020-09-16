<template>
  <v-container>
    <div class="headline">Resume ranker</div>
    <p class="mt-4 body-1 text-justify">
      This app allows the recruiter to identify and prioritise the most relevant
      candidates from a large pool of candidates, by ranking a provided set of
      profiles by relevance. It requires a provided set of input keywords
      (rankings are provided based on the number of keyword matches. Phrases in
      "Input keywords" must be separated into multiple lines as shown. Files are
      not stored across multiple uses. The relevance metric uses
      <a href="https://github.com/seatgeek/fuzzywuzzy#partial-ratio"
        >partial ratio</a
      >.
      <b>The only accepted file formats are .pdf and .docx.</b>
    </p>
    <v-textarea
      outlined
      auto-grow
      label="Input keywords"
      v-model="inputPhrases"
    />
    <v-file-input
      ref="files"
      show-size
      counter
      clearable
      multiple
      :loading="loading"
      accept=".docx, .pdf"
      v-model="files"
    />
    <v-btn
      class="mr-2"
      color="green lighten-3"
      :disabled="!files.length"
      @click="sendFile()"
    >
      <v-icon class="mr-2" left dark>mdi-cloud-upload</v-icon>
      Upload {{ files.length }} files
    </v-btn>
    <v-btn class="mr-2" @click="clear()" :disabled="inputPhrases == ``">
      <v-icon class="mr-2" left dark>mdi-cloud-refresh</v-icon>Clear
    </v-btn>
    <v-data-table
      v-if="results.length"
      class="elevation-1 mt-5 px-4"
      :headers="headers"
      :items="results"
    />
  </v-container>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  name: "FileUpload",
  data() {
    return {
      files: [],
      inputPhrases: `full stack python developer
django web development`,
      headers: [
        {
          text: "File Name",
          align: "end",
          value: "fileName"
        },
        { text: "Relevance", value: "score", sortable: true }
      ],
      results: [],
      loading: false
    };
  },
  methods: {
    sendFile() {
      let formData = new FormData();
      formData.append("inputPhrases", this.inputPhrases);

      _.forEach(this.files, file => {
        formData.append("files", file);
      });

      axios
        .post("/upload", formData)
        .then(response => {
          console.log(`Received server response:`);
          console.log(response.data);
          let entries = Object.entries(response.data);
          this.results = entries.map(item => ({
            fileName: item[0],
            score: item[1]
          }));
          this.loading = false;
        })
        .catch(error => {
          console.log(`Error: ${error}`);
        });

      this.loading = true;
      this.files = [];
    },
    clear() {
      this.files = [];
      this.inputPhrases = ``;
      this.results = [];
    }
  }
};
</script>
