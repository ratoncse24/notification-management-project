<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        md12
      >
        <div>
          <MaterialCard
            color="general"
            title="Notification List"
            text=""

          >
          
            <v-dialog
              v-model="dialog"
              max-width="500px">
              <template v-slot:activator="{ on }">
                <v-btn
                  id="newNotification"
                  color="general"
                  dark
                  class="mb-2"
                  v-on="on">New Notification</v-btn>
              </template>
              <v-card>
                <v-card-text>
                  <v-container grid-list-md >
                    <v-layout wrap>
                      <p>{{formTitle}}</p>
                      <v-form v-model="isFormValid">
                      <v-flex
                        xs12
                        sm12
                        md12>
                        <v-textarea
                          id="notification_text"
                          v-model="notification.notification_text"
                          label="Notifiction Text"
                          required
                          :rules="[() => !!notification.notification_text || 'This field is required']"
                           />
                      </v-flex>

                      <v-flex
                        xs12
                        sm12
                        md12>
                          <v-radio-group v-model="notification.event" label="Event" id="notification_event">
                            <v-radio
                                :disabled="editedIndex == -1 ? false : true"
                                v-for="event in events"
                                :key="event.value"
                                :label="event.text"
                                :value="event.value"
                            ></v-radio>
                            </v-radio-group>
                      </v-flex>
                      </v-form>
                    </v-layout>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer/>
                  <v-btn
                    id="cancelButton"
                    color="blue darken-1"
                    flat
                    @click="close">Cancel</v-btn>
                  <v-btn
                   :disabled="!isFormValid"
                    color="blue darken-1"
                    id="submitButton"
                    flat
                    @click="save">{{formButtonTitle}}</v-btn>
                </v-card-actions>
                  
              </v-card>
            </v-dialog>


            <v-data-table
              :headers="headers"
              :items="notifications"
              class="elevation-1"

            >
              <!-- change table header color(or other properties) -->
              <template
                slot="headerCell"
                slot-scope="{ header }"
              >
                <span
                  class="subheading font-weight-light text-general text--darken-3"
                  v-text="header.text"
                />
              </template>
              <template v-slot:items="props" >
                <td>{{ getEventTitle(props.item.event) }}</td>
                <td class="">{{ props.item.notification_text }}</td>
                <td class="justify-center " style="width: 15%">
                  <v-icon
                    medium
                    class="mr-2 edit-notification"
                    @click="editNotification(props.item)"
                  >
                    edit
                  </v-icon>
                  <v-icon
                  class="delete-notification"
                    medium
                    @click="deleteNotification(props.item)"
                  >
                    delete
                  </v-icon>
                </td>
              </template>
            </v-data-table>
          </MaterialCard>
        </div>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import MaterialCard from '@/components/material/Card.vue';

export default {
   components: {
            'MaterialCard': MaterialCard
    },
  data: () => ({
    isFormValid: false,
    color: 'general',
    snack: true,
    snackColor: '',
    snackText: '',
    pagination: {},
    dialog: false,
    headers: [
      { text: 'Event',align: 'left', value: 'event' },
      { text: 'Text', value: 'notification_text' },
      { text: 'Actions', value: 'name', sortable: false }
    ],
    events: [
      { text: 'First Visit', value: '1st-visit' },
      { text: 'Second Visit', value: '2nd-visit' },
      { text: 'Old users (after 1 months)', value: 'old-user-after-1-month' },
      { text: 'Returning users (After a purchase and revisited)', value: 'after-purchase-and-revisited' }
    ],
    notifications: [],
    editedIndex: -1,
    notification: {
      event: '1st-visit',
      notification_text: ''
      },
    defaultNotification: {
      event: '1st-visit',
      notification_text: ''
    }
  }),

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Notification' : 'Edit Notification'
    },
    formButtonTitle () {
      return this.editedIndex === -1 ? 'Save' : 'Update'
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    }
  },

  created () {
    this.initialize()
  },

  methods: {
    initialize () {
      this.fetchNotifications();
    },

    fetchNotifications(){
      // Fetch all notification from database
      this.$http.get('notification')
        .then((response) => 
          this.notifications = response.data
        )
        .catch(err => {
          console.log(err)
          this.snackbar = true
        })

    },

    getEventTitle(event_text){
      // get event title by event key
      var search_event =  this.events.filter(event => event.value == event_text)[0];
      if(search_event){
        return search_event.text
      }
    },

    editNotification (item) {
      // open edit notification form 
      this.editedIndex = this.notifications.indexOf(item)
      this.notification = Object.assign({}, item)
      this.dialog = true
    },

    deleteNotification (item) {
      // Method for delete notification 
      const index = this.notifications.indexOf(item)
      if(confirm('Are you sure you want to delete this notification?')){
        this.$http.delete('notification/'+item.id)
          .then((response) => {
            this.notifications.splice(index, 1)
            this.$notify({
              group: 'notification',
              type: 'success',
              title: 'success',
              text: 'Notification deleted successfully!'
            })
            }
          )
        .catch(err => {
          console.log(err)
          this.$notify({
              group: 'notification',
              type: 'warn',
              title: 'Failed',
              text: 'Notification delete fail.'
            })
        })
      }
    },

    close () {
      // close notification form dialog
      this.dialog = false
      setTimeout(() => {
        this.notification = Object.assign({}, this.defaultNotification)
        this.editedIndex = -1
      }, 300)
    },

    save () {
      // Create or Update notification 
      if (this.editedIndex > -1) {
        // update existing notification
        let notification = this.notifications[this.editedIndex]
        this.$http.put('notification/'+notification.id, this.notification)
          .then((response) => {
              Object.assign(this.notifications[this.editedIndex], this.notification)
              this.$notify({
              group: 'notification',
              type: 'success',
              title: 'success',
              text: 'Notification updated successfully!'
            })
            }
          )
        .catch(err => {
          console.log(err)
          this.$notify({
              group: 'notification',
              type: 'warn',
              title: 'Failed',
              text: 'Notification update failed.'
            })
        })
      } else {
        // Create new notification
        this.$http.post('notification', this.notification)
          .then((response) => {
            this.fetchNotifications()
            this.$notify({
              group: 'notification',
              type: 'success',
              title: 'success',
              text: 'New notification added successfully!'
            })
            }
          )
        .catch(err => {
          this.$notify({
              group: 'notification',
              type: 'warn',
              title: 'Failed',
              text: 'New notification creatin failed.'
            })
        })
      }
      this.close()
    }
  }
}
</script>

<style>
table.v-table thead tr {
  color: red !important;
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, .05);
}
</style>
