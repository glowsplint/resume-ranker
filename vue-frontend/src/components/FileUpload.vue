<template>
  <v-container>
    <!-- helpText="'Choose .pdf or .docx files'" -->
    <!-- type: 'Invalid file type. Only .pdf or .docx allowed', -->
    <!-- size: 'Files should not exceed 2MB in size' -->
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
      accept=".docx, .pdf"
      v-model="files"
    />
    <v-btn class="mt-2" :disabled="!files.length" @click="sendFile()"
      >Upload {{ files.length }} files</v-btn
    >
    <v-btn class="mt-2 ml-2" @click="reset()">Reset</v-btn>
  </v-container>
</template>

<script>
// https://www.youtube.com/watch?v=dxgbgYtNzCw
import axios from "axios";
import _ from "lodash";

export default {
  name: "FileUpload",
  data() {
    return {
      files: [],
      message: "",
      error: false,
      inputPhrases: `python developer
full stack web development
django frontend`
    };
  },
  methods: {
    sendFile() {
      // The first item in the form is the inputPhrase string, the rest are the files
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
        })
        .catch(error => {
          console.log(`Error: ${error}`);
        });

      this.inputPhrases = "";
      this.message = "Files have been uploaded";
      this.files = [];
    },
    reset() {
      this.files = [];
      this.message = "";
      this.error = false;
      this.inputPhrases = `python developer
full stack web development
django frontend`;
    }
  }
};
</script>
